"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)

    data = [] # The data that will be returned, separate instance from data in main
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like

        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts

        print(parts)  # See what the parts look like (notice the integer is a string)

        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)

        print(parts)  # See if that worked
        print("----------")
        data.append(parts) # Add parts to data
    input_file.close()
    return data # Return data as a list of lists

def display_subjects_details(data):
    """ prints subject data in worded format for each record"""
    for record in data:
        print(f"{record[0]} is taught by {record[1]} and has {record[2]} students")

main()