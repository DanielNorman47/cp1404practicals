"""
CP1404 - Intermediate Exercise
wimbledon
Estimate: 20m
Actual: 41m
"""
FILENAME = "wimbledon.csv"


def main():
    champions_to_data = {}  # {champion: (country, win count), champion: (...}
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip the first record (headers)
        for line in in_file:
            data = line.split(",")  # index 1 = country, index 2 = winner name
            process_record(data[2], data[1], champions_to_data)
    print_champions(champions_to_data)
    print_countries(champions_to_data)


def print_countries(champions_to_data):
    """print all countries that had winners in alphabetical order"""
    # get a set (so no dupes) of the countries VVV
    countries = set(country[0] for country in champions_to_data.values())
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(" ".join(sorted(countries)))  # smoosh all countries into 1 string


def print_champions(champions_to_data):
    """print all champions and their win counts"""
    for record in champions_to_data.items():
        name = record[0]
        win_count = record[1][1]
        print(f"{name} {win_count}")


def process_record(name, country, champions_to_data):
    """creates new record in champions dict or increases their win count"""
    try:  # attempt to increase their win count
        champions_to_data[name][1] += 1
    except KeyError:  # create new record if not exist
        champions_to_data[name] = [country, 1]
    # no return is needed as the passed func side dict is an alias of main's one


main()
