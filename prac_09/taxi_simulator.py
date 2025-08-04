"""
taxi simulate DFS exercise
cp1404
"""
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi
MENU_MESSAGE = "q)uit, c)hoose taxi, d)rive\n"
def main():
    """allow users to choose a taxi and drive a distance getting their bill at the end."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    # the selected taxi
    current_taxi = None # placeholder for until one is selected
    choice = input(MENU_MESSAGE).upper()
    while choice != "Q":
        if choice == "C":
            print_taxis(taxis)
            taxi_index = input("Choose taxi: ")
            try:
                current_taxi = taxis[int(taxi_index)]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "D":
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
        else:
            print("Invalid option")
        print(f"Bill to date: ${sum(taxi.get_fare() for taxi in taxis):.2f}")
        choice = input(MENU_MESSAGE).upper()

def print_taxis(taxis):
    """print all taxis with their index"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()