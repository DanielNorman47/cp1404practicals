"""Basic list operations"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    """ask user for 5 numbers then display the 1st, last, min, max, and average"""

    # check if user is allowed
    if is_authorised_user():

        print("Access granted")
        numbers = populate_numbers() # get 5 numbers from user and return in list

        #print miscellaneous information
        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average of the numbers is {sum(numbers)/len(numbers)}")
    else:
        print("Access denied")


def populate_numbers():
    """gets user to input 5 numbers and adds them to list"""
    numbers = []
    for i in range(0, 5): # i is not used. Is there a better way to do this without creating an obsolete variable?
        number = int(input("Enter number: ")) # get number from user
        numbers.append(number) # add number to list
    return numbers # return list

def is_authorised_user():
    """is user inputted username in authorised user list"""
    return input("username: ") in usernames

main()