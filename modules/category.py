from enum import Enum

class Catergory(Enum):
    LIVNG = 1
    FOOD = 2
    TRAVEL = 3
    SAVING = 4
    LEISURE = 5

    @classmethod
    def get_categories(cls):
        pass
