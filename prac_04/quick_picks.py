"""quick pick lottery ticket generator"""
import random
from xml.etree.ElementTree import tostring


def main():
    """print as many tickets as user requests"""
    number_of_tickets = int(input("How many quick picks? "))
    tickets = [] # list of lists tickets[x] is the xth ticket and is a list
    for i in range(number_of_tickets):
        tickets.append(sorted(create_ticket())) # add 1 ticket at a time to tickets
    print_tickets(tickets) # print all results

def print_tickets(tickets):
    """prints tickets to match the given formatting"""
    for ticket in tickets:
        print(" ".join([f"{number:>2}" for number in ticket]))


def create_ticket():
    numbers = [] # final ticket output
    for i in range(0, 6): # loop 6 times

        # while number is duplicate reroll number
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number) #add valid number to numbers
    return numbers # return numbers (a complete ticket)

main()
