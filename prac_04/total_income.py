"""
CP1404/CP5632 Practical
Complete code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    populate_incomes(incomes, number_of_months)

    print_report(incomes)


def populate_incomes(incomes, number_of_months):
    """populates incomes with user inputs"""
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)


def print_report(incomes):
    """prints monthly and cumulative income in report format"""
    print("\nIncome Report\n-------------")
    total = 0
    # number_of_months was removed as an argument and replaced with...
    # len(incomes), which is the same
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()