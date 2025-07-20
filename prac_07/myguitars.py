"""Get guitars from file and move into guitar objects"""
FILE = "guitars.csv"
import csv
import guitar

def main():
    """Read guitars from file and move into guitar object list"""
    guitars = []
    with open(FILE, 'r', newline='') as csvfile:
        for row in csv.reader(csvfile):
            name = row[0]
            year = int(row[1])
            cost = float(row[2])
            guitar_object = guitar.Guitar(name=name, year=year, cost=cost)
            guitars.append(guitar_object)
            print(guitar_object)

    guitars.sort()


main()