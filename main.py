import os
from aiget import sendQuestion
from dataio import loadAPIKeys, loadTickets, saveTickets

from globals import FILENAME, APIKeys, UseDialogMode, bcolors
from globals import Tikets
from question import AIQuestion
from templates import CodeCommands
from templates import *
from globals import Question


def onProgramStart():
    # try:
    APIKeys = loadAPIKeys()
    print("API Keys: ")
    print(APIKeys)
    # except Exception:
    # print("API Keys not loaded!")
    # print(Exception)
    # exit(-1);

    if os.path.exists(FILENAME):
        Tickets = loadTickets(FILENAME)
        print("Tickets data loaded!\n")
    else:
        print("File not foun or first launch, new repository created \n")


def onProgramClose():
    print("Saving tickets\n")
    saveTickets(FILENAME, Tikets)


def startScreen():
    print("Добро пожаловать в OpenAI Code help!\n")
    print("Эта программа предназначенна для кодогенерации на различных ЯП, посредством OpenGPT-3\n")


def enterQuestion() -> AIQuestion:
    if not UseDialogMode:
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
        cmd = CodeCommands
        template = Templates[command]
        template.data = fillObjectAttributes(template.data)
        template.data.Language = language

        quest: AIQuestion = AIQuestion(template.tempStr, template.data,
                                       theme, language, command
                                       )
    else:
        quest = AIQuestion(startvalue=Question)
    return quest


def main():
    onProgramStart()
    startScreen()
    while True:
        print("\n")
        global Question
        Question = input(">> ")
        if Question == "exit":
            break
        quest = enterQuestion()
        print(
            f"\n{bcolors.OKGREEN}<<{sendQuestion(quest.genquest)}")
        print(bcolors.ENDC)

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
