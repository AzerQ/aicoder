from datetime import datetime
import datetime
from uuid import UUID
import uuid
from aiget import sendQuestion


# Базовый класс вопроса
class AIQuestion:
    id: UUID  # Уникальный идентификатор вопроса
    time: datetime.datetime  # Время вопроса
    queststr: str  # Строка вопроса
    theme: str  # Тема топика
    language: str  # Язык программирования
    GenerateTheme: bool  # Генерировать ли тему вопроса

    def __init__(self,
                 queststr: str,
                 theme: str = "",
                 language: str = "",
                 generateTheme=False
                 ) -> None:
        self.GenerateTheme = generateTheme
        self.queststr = queststr
        self.language = language
        self.theme = sendQuestion(
            f'Get me theme of this question: "{self.queststr}"') if theme == "" and self.GenerateTheme else theme
        self.id = uuid.uuid4()
        self.time = datetime.datetime.now()

    # Сгенерировать ответ
    def getAnwser(self, mode) -> str:
        self.time = datetime.datetime.now()
        return sendQuestion(question=self.queststr,mode=mode)
