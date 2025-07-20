"""
Project Management exercise
Guess time: 45m
Actual time:
"""

DEFAULT_FILE = "projects.txt"
CHOICE_MESSAGE = "Select a Menu"\
                 "L - Load Projects\nS - Save Projects\n"\
                 "D - Display Projects\nF - Filter Projects\n"\
                 "A - Add Project\nU - Update Project\n"\
                 "Q - Quit"


def main():
    choice = input(CHOICE_MESSAGE).upper()  # The desired selected menu
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid menu choice")
        choice = input(CHOICE_MESSAGE).upper()
    # To save or not to save


def load_projects():
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects():
    pass


def add_project():
    pass


def update_project():
    pass


# name = input("Name: ")  # for while loop condition
# guitars = []
# while name != "":
#     year = int(input("Year: "))
#     cost = int(input("Cost: ").replace("$", ""))
#
#     guitars.append(Guitar(name, year, cost))
#     name = input("Name: ")  # loop to next guitar or quit

main()
