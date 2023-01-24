import json

from ticketrepo import TicketRepository


def loadTickets(filename: str) -> TicketRepository:
    repo: TicketRepository = None
    with open(filename, 'r') as data_file:
        rep:list[Ticket] = json.load(data_file)
        repo = TicketRepository(rep)
    return repo


def saveTickets(filename: str, repo: TicketRepository):
    with open(filename, 'w') as f:
        json.dump(repo.tickets, f, ensure_ascii=False, indent=4)


def loadAPIKeys(filename: str = "OpenAIKeys.json") -> list[str]:
    res: object
    with open(filename, 'r') as data_file:
        res = json.load(data_file)
    #print(res)
    return res["OpenAIKeys"]
