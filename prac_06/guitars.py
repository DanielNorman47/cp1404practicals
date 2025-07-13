"""
guitars for DFS exercise
Expected time: 15m
Actual time: 12m
"""
from guitar import Guitar


def main():
    """get users guitars from inputs and print them all"""
    print("My guitars!")
    name = input("Name: ")  # for while loop condition
    guitars = []
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: ").replace("$", ""))

        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")  # loop to next guitar or quit

    # print guitars
    for i, guitar in enumerate(guitars, 1):
        print(
            f"Guitar {i}: {guitar.name:>10} ({guitar.year}), worth ${guitar.cost:8,.2f}{"(vintage)" if guitar.is_vintage() else ""}")


main()
