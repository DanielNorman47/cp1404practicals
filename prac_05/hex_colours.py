"""CP1404 - Intermediate Exercise"""
COLOUR_NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a",
                       "aliceblue": "#f0f8ff", "alizarin crimson": "#e32636",
                       "amaranth": "#e52b50", "amber": "#ffbf00",
                       "amethyst": "#9966cc", "antiquewhite": "#faebd7",
                       "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}


def main():
    """User inputs colour's name and its colour code"""
    #get colour name from user without caps
    colour_name = input("Enter colour name: ").lower()
    try:
        colour_code = COLOUR_NAME_TO_CODE[colour_name]
        print("Colour code: ", colour_code)
    except KeyError:
        print("Invalid colour name.")
main()
