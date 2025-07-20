"""
Project Management exercise
Guess time: 45m   ->  changed to 1.5 hours 23 minutes in
Actual time:
"""

import datetime
import project

from prac_03.capitalist_conrad import out_file

DEFAULT_FILE = "projects.txt"
CHOICE_MESSAGE = "Select a Menu\n" \
                 "L - Load Projects\nS - Save Projects\n" \
                 "D - Display Projects\nF - Filter Projects\n" \
                 "A - Add Project\nU - Update Project\n" \
                 "Q - Quit\n"


def main():
    projects = []  # will NOT be global but most funcs will need access to it
    get_projects_from_file(projects, DEFAULT_FILE)
    choice = input(CHOICE_MESSAGE).upper()  # The desired selected menu
    while choice != "Q":
        if choice == "L":
            load_projects(projects)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
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


def get_projects_from_file(projects, file_name):
    """get projects from file and add to list"""
    with open(file_name, "r") as file:
        file.readline()  # skip header
        for line in file:
            parts = line.split("\t")  # split by the tabs
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()  # get date in date object format
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = float(parts[4])
            projects.append(project.Project(name, start_date, priority, cost_estimate, completion_percentage))


def give_projects_to_file(projects, file_name):
    """get projects from list and add to file"""
    with open(file_name, "w") as output_file:
        print("Name	Start Date  Priority	Cost Estimate	Completion Percentage", file=output_file)  # add header
        for project_object in projects:
            date = datetime.datetime.strftime(project_object.start_date, "%d/%m/%Y")
            line = "\t".join([project_object.name, date, project_object.priority, project_object.cost_estimate, project_object.completion_percentage])
            print(line, file=output_file)


def load_projects(projects):
    """get user file name and send to get_projects_from_file"""
    file_name = input("What file would you like to load:\n")
    get_projects_from_file(projects, file_name)


def save_projects(projects):
    """get user file name and send to give_projects_to_file"""
    file_name = input("What file would you like to load:\n")
    give_projects_to_file(projects, file_name)


def display_projects(projects):
    for i, project_object in enumerate(projects):
        print(f"{i+1} - {project_object}")


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
