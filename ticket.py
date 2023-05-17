from __future__ import annotations
import json
from uuid import UUID
from question import AIQuestion
from datetime import datetime
from uuid import UUID
import datetime


class Ticket:
    id: UUID
    anwser: str
    quest: AIQuestion

    def __init__(self, anwser: str, quest: AIQuestion) -> None:
        self.anwser = anwser
        self.quest = quest
        self.id = quest.id

# region Репозиторий тикетов


class TicketRepository:

    tickets: list[Ticket]

    def __init__(self):
        self.tickets = []

    def __init__(self, tickets: list[Ticket]):
        self.tickets = tickets

    def getAll(self):
        return self.tickets

    def getByDate(self, dateStart: datetime, dateEnd: datetime = datetime.datetime.now()):
        res: list[Ticket] = []
        for ticket in self.tickets:
            if (ticket.quest.time > dateStart and ticket.quest.time < dateEnd):
                res.append(ticket)
        return TicketRepository(res)

    def getByTheme(self, theme: str) -> TicketRepository:
        res: list[Ticket] = []
        for ticket in self.tickets:
            if (ticket.quest.theme == theme):
                res.append(ticket)
        return TicketRepository(res)

    def getByLang(self, lang: str) -> TicketRepository:
        res: list[Ticket] = []
        for ticket in self.tickets:
            if (ticket.quest.language == lang):
                res.append(ticket)
        return TicketRepository(res)

    def getById(self, id: UUID) -> Ticket:
        res: list[Ticket] = []
        for ticket in self.tickets:
            if (ticket.id == id):
                return ticket
        return None
# endregion

# region Загрузка/сохранение тикетов


def loadTickets(filename: str) -> list[dict[str, (str, str)]]:
    res: list[dict[str, (str, str)]] = []
    #with open(filename, 'r') as data_file:
        #res = json.load(data_file)
    return res


def saveTickets(filename: str, tickets: list[dict[str, (str, str)]]):
    #with open(filename, 'w', encoding='utf-8') as f:
        #json.dump(tickets, f, ensure_ascii=False, indent=4)
    pass
# endregion
