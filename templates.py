from enum import Enum
import enum


class QuestionTemplate:
    tempstring: str  # Строка шаблона
    replacevals: dict[str, str]  # Заменяемые значения

    def __init__(self, data: dict[str, str], tempStr: str) -> None:
        self.replacevals = data
        self.tempstring = tempStr

    def generateString(self) -> str:
        return self.tempstring.format(**self.replacevals)

    def inputVals(self) -> dict[str, str]:
        print(f"Шаблонная строка: {self.tempstring}")
        for key in self.replacevals:
            self.replacevals[key] = input(
                f"Введите значение [{key}] в шаблоне: ")
        return self.replacevals


# region Шаблоны вопросов К ИИ
functionTemp = '''Generate function with {Arguments} for {Description}
and return {Return} on {Language} programming language'''

classTemp = '''Generate class for {Description}
on {Language} programming language'''

enumTemp = '''Generate enum of {EnumTheme} on {Language} programming language'''

mockDataTemp = '''Generate {Count} mock data objects with scheme = {DataScheme}
using {Language} language'''

anyQuestionTemp = "{Description}"

# endregion

# region Data-классы для шаблонов вопросов


class BaseData:
    Language: str = ''

    def __init__(self) -> None:
        pass


class FunctionData(BaseData):
    Arguments: str = ''
    Description: str = ''
    Return: str = ''


class ClassData(BaseData):
    Description: str = ''


class EnumData(BaseData):
    EnumTheme: str = ''


class MockData(BaseData):
    Count: str = ''
    DataScheme: str = ''


class AnyQuestionData(BaseData):
    Description: str = ''


shortNames = {

}
# endregion

# region Шаблоны


@enum.unique
class CodeCommands(enum.IntEnum):
    Function = 1
    Class = 2
    Enum = 3
    MockData = 4
    AnyQuestion = 5


Templates = {
    CodeCommands.Function: QuestionTemplate(vars(FunctionData()), functionTemp),
    CodeCommands.Class: QuestionTemplate(vars(ClassData()), classTemp),
    CodeCommands.Enum: QuestionTemplate(vars(EnumData()), enumTemp),
    CodeCommands.MockData: QuestionTemplate(vars(MockData()), mockDataTemp),
    CodeCommands.AnyQuestion: QuestionTemplate(
        vars(AnyQuestionData()), anyQuestionTemp)
}

# endregion
