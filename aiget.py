import random
import os
import openai
from dataio import loadAPIKeys

from globals import APIKeys

# Отослать вопрос OpenAI


def sendQuestion(question: str) -> str:
    keys = loadAPIKeys()
    index = random.randint(0, len(keys)-1)
    openai.api_key = keys[index]
    res =  openai.Completion.create(model="text-davinci-003",
                                   prompt=question,
                                   temperature=0.7, 
                                   max_tokens=3700,
                                   top_p=1,
                                   frequency_penalty=0,
                                   presence_penalty=0)
    return res.choices[0].text
