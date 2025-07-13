"""class for programming languages"""


class ProgrammingLanguage:
    """class for programming languages"""

    def __init__(self, name, typing, reflection, year):
        """initialisation"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """boolean - if the language is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """string returns all self variables"""
        return f"{self.name}, {self.typing}, {self.reflection}, {self.year}"
