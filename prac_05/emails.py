"""
CP1404 - Intermediate Exercise
Emails occurrences
Estimate: 15m
Actual: 11m
"""


def main():
    """allow user to store emails to names in dictionary and list them all"""
    emails_to_names = {}
    email = input("Email: ")
    while email != "":  # while email is not blank
        name = name_from_email(email)
        if input(f"Is your name {name}? (Y/n)").lower() == "n":
            name = input("Name: ")  # get actual name
        # no else needed, as name before @ is correct
        emails_to_names[email] = name
        email = input("Email: ")  # ask for another email to complete loop
    print_data(emails_to_names)


def print_data(emails_to_names):
    """print all names and emails"""
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def name_from_email(email):
    """convert from email to name by removing everything after @"""
    return email.split("@")[0]


main()
