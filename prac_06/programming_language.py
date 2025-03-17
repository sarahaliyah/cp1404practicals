"""
Estimated time: 20 minutes
Time taken: 30 minutes
"""


class ProgrammingLanguage:
    """Represent information of a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage with name, typing, reflection, and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a formatted string describing the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the programming language uses dynamic typing."""
        return self.typing == "Dynamic"


def run_tests():
    """Run and test ProgrammingLanguage instances, printing dynamically typed languages."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
