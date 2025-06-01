""" score menu"""
import score
def main():
    score_value: int = 0
    MENU = ("(G)et a valid score\n"
    '(P)rint result\n'
    '(S)how stars\n'
    '(Q)uit\n')
    option = input(MENU).upper()
    while option != "Q":
        if option == "G":
            score_value = get_valid_score()
        elif option == "P":
            print_result(score_value)
        elif option == "S":
            print_stars(score_value)
        else:
            print("Exception, input a valid score")
        option = input(MENU).upper()

def get_valid_score():
    return int(input("Enter your score: "))

def print_result(score_value):
    result = score.convert_score_to_result(score_value)
    print(f"Your result is: {result}")

def print_stars(score_value):
    print("*" * score_value)

main()
