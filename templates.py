from enum import Enum
import enum

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


@enum.unique
class CodeCommands(enum.IntEnum):
    Function = 1
    Class = 2
    Enum = 3
    MockData = 4
    AnyQuestion = 5


class Template:
    data: BaseData
    tempStr: str

    def __init__(self, data: BaseData, tempStr: str) -> None:
        self.data = data
        self.tempStr = tempStr


Templates = {
    CodeCommands.Function: Template(FunctionData(), functionTemp),
    CodeCommands.Class: Template(ClassData(), classTemp),
    CodeCommands.Enum: Template(EnumData(), enumTemp),
    CodeCommands.MockData: Template(MockData(), mockDataTemp),
    CodeCommands.AnyQuestion: Template(AnyQuestionData(), anyQuestionTemp)
}
