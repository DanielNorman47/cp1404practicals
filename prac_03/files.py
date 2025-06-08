"""
files
"""
from prac_03.capitalist_conrad import out_file

NAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"

def main():
    # write_name()
    # print_name_from_file()
    # sum_first_two_numbers()
    sum_all_numbers()


def write_name():
    name = input("Enter your name: ")
    out_file_name = open(NAME_FILE, "w")
    out_file_name.write(name)
    out_file_name.close()

def print_name_from_file():
    out_file_name = open(NAME_FILE, "r")
    print(f"Hi {out_file_name.readline()}!")

def sum_first_two_numbers():
    with open(NUMBER_FILE, "r") as in_file_number:
        first_number = int(in_file_number.readline())
        second_number = int(in_file_number.readline())
    print(first_number + second_number)

def sum_all_numbers():
    total = 0 #declaration for += usage
    with open(NUMBER_FILE, "r") as in_file_number:
        for line in in_file_number:
            total += int(line)
    print(total)

main()