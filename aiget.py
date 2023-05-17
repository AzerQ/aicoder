from enum import Enum
import random
import openai
from dataio import loadAPIKeys


class AIMode(Enum):
    Text = 0,
    Code = 1,
    Image = 2
# Отослать вопрос OpenAI


def getRandomKey() -> str:
    keys = loadAPIKeys()
    index = random.randint(0, len(keys)-1)
    return keys[index]


def sendQuestion(question: str, mode: AIMode=AIMode.Text) -> str:
    openai.api_key = getRandomKey()
    try:
        if mode == AIMode.Image:
            image_resp = openai.Image.create(
                prompt=question, n=1, size="1024x1024")
            return image_resp['data'][0]['url']

        elif mode == AIMode.Text:
            res = openai.Completion.create(model="text-davinci-003",
                                           prompt=question,
                                           temperature=0.7,
                                           max_tokens=3000,
                                           top_p=1,
                                           frequency_penalty=0,
                                           presence_penalty=0,
                                           stop=["Human:", "AI:"])
            return res.choices[0].text

        elif mode == AIMode.Code:
            res = openai.Completion.create(model="code-davinci-002",
                                           prompt=question,
                                           temperature=0.7,
                                           max_tokens=3800,
                                           top_p=1,
                                           frequency_penalty=0,
                                           presence_penalty=0,
                                           )
            return res.choices[0].text
    except Exception as exc:
        return f"AI Сервер не отвечает... с ошибкой {exc}"
