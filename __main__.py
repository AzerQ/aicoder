import datetime
import os
import argparse
import sys
from sys import platform
from aiget import AIMode
from codelangs import CodeLangs
from dataio import loadAPIKeys
from globals import FILENAME, UseDialogMode, bcolors
from globals import tickets
from question import AIQuestion
from templates import CodeCommands
from templates import *
from ticket import Ticket
from ticket import loadTickets, saveTickets
import pyperclip as clipboard
import urllib.request


def onProgramStart():
    if os.path.exists(FILENAME):
        try:
            global tickets
            globals.Tickets = loadTickets(FILENAME)
            print("Tickets data loaded!\n")
        except Exception as exc:
            print(f"History file founded, by parsing exception occured {exc}")
    else:
        print("File not foun or first launch, new repository created \n")


def onProgramClose():
    print("Saving tickets\n")
    saveTickets(FILENAME, tickets)


def startScreen():
    print("Добро пожаловать в OpenAI Code help!\n")
    print("Эта программа предназначенна для кодогенерации на различных ЯП, посредством OpenGPT-3\n")


def enterQuestion() -> AIQuestion:
    print("Добро пожаловать в меню ввода вопроса--->\n")
    command: CodeCommands = None
    choise: int = int(input('''Выберете тип комманды:\n
        1) Генерация функции\n
        2) Генерация класса\n
        3) Генерация перечисления\n
        4) Генерация мок-данных\n
        5) Обычный вопрос\n
        Ваш выбор: 
        '''))
    command: CodeCommands = CodeCommands(choise)
    language = input("Введите язык программирования: ")
    theme = input("Введите тему (необязательно): ")
    theme = theme if theme != "" else "default"
    myTemplate = Templates[command]
    myTemplate.inputVals()
    quest: AIQuestion = AIQuestion(
        myTemplate.generateString(),
        theme, language
    )
    return quest


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description="Question argument parser")
    parser.add_argument('-inp', default="NONE", type=str,
                        help="Input text file path")
    parser.add_argument('-out', default="NONE", type=str,
                        help="Anwser text file path")
    parser.add_argument("-m", default=AIMode.Text.name, type=str,
                        help="AI Model Mode")
    parser.add_argument("-q", default="NONE", type=str,
                        help="Question to OpenAI GPT-3")
    parser.add_argument('--f', action="store_true", help="Off console colors")
    parser.add_argument('--pt', action="store_true",
                        help="On time marks in chat")
    args = parser.parse_args()
    mode = AIMode[args.m]
    # print(args.m)
    if (args.inp != "NONE"):
        with open(args.inp, 'r', encoding='utf-8') as file:
            data = file.read()
            result = AIQuestion(data).getAnwser(mode)
            if (args.out != "NONE"):
                with open(args.out, 'w', encoding='utf-8') as outfile:
                    outfile.write(result)
            else:
                print(result)
            exit(0)

    if (args.q != "NONE"):
        prefix = "" if args.f else bcolors.OKGREEN

        if (args.out != "NONE"):
            file_ext: str = os.path.splitext(args.out)[1]
            postfix: str = CodeLangs[file_ext] if file_ext in CodeLangs else ""
            quest = args.q + \
                f" write it on {postfix} programming language" if postfix != "" else args.q
            result = AIQuestion(quest).getAnwser(mode)
            if mode == AIMode.Image:
                req = urllib.request.Request(
                    result, headers={'User-Agent': 'Mozilla/5.0'})
                with open(args.out, "wb") as f:
                    with urllib.request.urlopen(req) as r:
                        f.write(r.read())
            else:
                with open(args.out, 'w', encoding='utf-8') as outfile:
                    outfile.write(result)

        else:
            result = AIQuestion(args.q).getAnwser(mode)
            print(
                f"\n{prefix}{result}")
        if not args.f:
            print(bcolors.ENDC)
        exit(0)
    else:
        onProgramStart()
        startScreen()
        global tickets
        complexQuestion: str = ''
        while True:
            quest: AIQuestion
            questionstr = input(">> ")
            if questionstr == "cls":
                if platform == "win32":
                    os.system("cls")
                else:
                    os.system("clear")
                continue
            if questionstr == "exit":
                break
            if "cnt" in questionstr:
                questionstr = questionstr.replace("cnt", " ")
                complexQuestion += "\nHuman: " + questionstr + "\nAI:"
            if "file" in questionstr:
                questionstr = questionstr.replace("file", "")
                questionstr = questionstr.replace('"', "")
                questionstr = questionstr.strip()
                fstr: str = ""
                with open(questionstr, 'r', encoding='utf-8') as file:
                    fstr = file.read()
                questionstr = fstr
                print("Question from file with content: " + questionstr)
                # print(complexQuestion)
            else:
                complexQuestion = questionstr
                #print(complexQuestion)
            if not UseDialogMode:
                quest = enterQuestion()
            else:
                quest = AIQuestion(queststr=complexQuestion)
            if args.pt:
                print(
                    f'{bcolors.HEADER}>> Question at time ({quest.time.strftime("%d-%b-%Y (%H:%M:%S)")})\n')
            anwser = quest.getAnwser(mode)
            complexQuestion += anwser
            if args.pt:
                print(
                    f'{bcolors.OKCYAN}<< Anwser at time {datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")}')
            print(
                f"{bcolors.OKGREEN}<<{anwser}")
            #clipboard.copy(anwser)
            print(bcolors.ENDC)
            tickets.append(
                {complexQuestion: (quest.time.strftime("%d-%b-%Y (%H:%M:%S)"), anwser)})
        onProgramClose()

# Получение всех свойств объекта


def getProps(obj: object, exclude: list[str] = []) -> list[str]: return [a for a in dir(obj) if not a.startswith(
    '__') and not a in exclude]


def fillObjectAttributes(obj: object) -> object:
    # print(obj.Language)
    props = getProps(obj, ["Language"])
    # print(props)
    for prop in props:
        setattr(obj, prop, input('Введите свойство "' + prop + '": '))
    return obj


if __name__ == "__main__":
    main()
