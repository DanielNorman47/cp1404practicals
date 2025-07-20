"""Get guitars from file and move into guitar objects"""
FILE = "guitars.csv"
import csv
import guitar


def main():
    """Read guitars from file and move into guitar object list"""
    guitars = []  # create empty list for guitars to go
    load_guitars(guitars)  # get guitars from csv and add to list
    get_guitar(guitars)  # ask user for new guitars
    guitars.sort()  # sort them by age
    save_guitars(guitars)

def save_guitars(guitars):
    """open csv file and print all guitars into it using string formating"""
    with open(FILE, 'w', newline='') as csvfile:
        for guitar_object in guitars:
            print(f"{guitar_object.name},{guitar_object.year},{guitar_object.cost}", file=csvfile)


def get_guitar(guitars):
    """get guitar from user input and add to parameter list"""
    name = input("Name: ")  # for while loop condition
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: ").replace("$", ""))
        guitar_object = guitar.Guitar(name, year, cost)
        guitars.append(guitar_object)
        print(f"Added {guitar_object} to guitars list")
        name = input("Name: ")  # loop to next guitar or quit


def load_guitars(guitars):
    """load all guitars from csv file"""
    with open(FILE, 'r', newline='') as csvfile:
        for row in csv.reader(csvfile):
            name = row[0]
            year = int(row[1])
            cost = float(row[2])
            guitar_object = guitar.Guitar(name=name, year=year, cost=cost)
            # variable name "guitar" overlaps with class name so isn't used here
            guitars.append(guitar_object)
            print(guitar_object)


main()
