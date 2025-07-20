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
            display_projects(projects, True)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        choice = input(CHOICE_MESSAGE).upper()
    # To save or not to save TODO


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


def display_projects(projects, index=False): # index is if it should display an index
    """display all projects with an index"""
    for i, project_object in enumerate(projects):
        print(f"{(i + 1) if index else ""} - {project_object}")


def filter_projects(projects):
    """get date from user, get projects after date, sort projects by date, display projects"""
    date = get_date_from_user()
    print(date)
    projects_after = [project_object for project_object in projects if project_object.is_start_after_date(date)]
    projects_after.sort()
    display_projects(projects_after)


def get_date_from_user():
    """get datetime.date formated date from user"""
    return datetime.datetime.strptime(input("Date (d/m/yyyy): "), "%d/%m/%Y").date()

def add_project(projects):
    """get user input to add a project to list"""
    name = input("Name: ")  # for while loop condition
    guitars = []
    while name != "":
        start_date = get_date_from_user()
        priority = int(input("Priority: "))
        cost = float(input("Cost Estimate: $"))
        percentage = int(input("Percentage: %"))
        guitars.append(project.Project(name, start_date, priority, cost, percentage))
        name = input("Name: ")  # loop to next project or quit


def update_project(projects):
    """update completion% and priority"""
    display_projects(projects)
    index = int(input("Select Project Index(1, 2, 3...: ")) - 1
    priority = f"Set {projects[index].name}'s priority to\ne.g. 1,2,3 or string for no change: "
    try:
        projects[index].priority = int(priority)
    except ValueError:
        print("Priority was not changed")

    percentage = f"Set {projects[index].name}'s priority to\ne.g. 1,2,3 or string for no change: "
    try:
        projects[index].priority = int(percentage)
    except ValueError:
        print("Priority was not changed")


main()
