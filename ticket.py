from uuid import UUID

from question import AIQuestion


class Ticket:
    id: UUID
    anwser: str
    quest: AIQuestion

    def __init__(self, anwser: str, quest: AIQuestion) -> None:
        self.anwser = anwser
        self.quest = quest
        self.id = quest.id