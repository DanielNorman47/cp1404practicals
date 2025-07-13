"""
Intermediate Exercise - languages
Guess time: 15m
Actual time:
"""
from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

print("\nThe dynamically typed languages are:")
languages = [python, visual_basic, ruby]
for language in languages:
    if language.is_dynamic():
        print(language.name)
