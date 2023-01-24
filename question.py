from datetime import datetime
import datetime
from uuid import UUID
import uuid


from templates import CodeCommands


# Базовый класс вопроса
class AIQuestion:
    id: UUID  # Уникальный идентификатор вопроса
    time: datetime  # Время вопроса
    genquest: str  # Сгенерированный вопрос
    tempalte: str  # Шаблон
    params: dict[str, str]  # Парметры шаблона
    theme: str  # Тема топика
    language: str  # Язык программирования
    codecommand: CodeCommands = CodeCommands.AnyQuestion  # Команда генерации кода

    def __init__(self, template: str = "", params: object = None,
                 theme: str = "",
                 language: str = "", command: CodeCommands = CodeCommands.AnyQuestion,
                 startvalue: str = "") -> None:
        self.language = language
        self.theme = theme
        if params != None:
            self.params = vars(params)
        self.tempalte = template
        self.id = uuid.uuid4()
        self.time = datetime.datetime.now()
        self.codecommand = command
        if startvalue == "":
            self.regenerateQuestion()
        else:
            self.genquest = startvalue

    # Сгенерировать вопрос

    def regenerateQuestion(self) -> str:
        self.genquest = self.tempalte.format(**self.params)
        print(self.genquest + "\n")
        return self.genquest
