from ticket import TicketRepository

# Загрузить API ключи
# APIKeys:list[str] = []

# Все глобальные тикеты программы

tickets: list[dict[str, (str, str)]] = []  # Глобальный репозиторий тикетов

FILENAME = "Tickets.json"  # Имя файла с историей запросов

UseDialogMode = True


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
