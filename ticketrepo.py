from __future__ import annotations
from datetime import datetime
from uuid import UUID
from templates import CodeCommands
from ticket import Ticket
import datetime


class TicketRepository:

    tikets: list[Ticket]

    def __init__(self):
        self.tikets = []

    def __init__(self, tickets: list[Ticket]):
        self.tikets = tickets

    def getAll(self):
        return self.tikets

    def getByDate(self, dateStart: datetime, dateEnd: datetime = datetime.datetime.now()):
        res: list[Ticket] = []
        for ticket in self.tikets:
            if (ticket.quest.time > dateStart and ticket.quest.time < dateEnd):
                res.append(ticket)
        return TicketRepository(res)

    def getByTheme(self, theme: str) -> TicketRepository:
        res: list[Ticket] = []
        for ticket in self.tikets:
            if (ticket.quest.theme == theme):
                res.append(ticket)
        return TicketRepository(res)

    def getByLang(self, lang: str) -> TicketRepository:
        res: list[Ticket] = []
        for ticket in self.tikets:
            if (ticket.quest.language == lang):
                res.append(ticket)
        return TicketRepository(res)

    def getByCommand(self, command: CodeCommands) -> TicketRepository:
        res: list[Ticket] = []
        for ticket in self.tikets:
            if (ticket.quest.codecommand == command):
                res.append(ticket)
        return TicketRepository(res)

    def getById(self, id:UUID) -> Ticket:
        res: list[Ticket] = []
        for ticket in self.tikets:
            if (ticket.id == id):
                return ticket
        return None
