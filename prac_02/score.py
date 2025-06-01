""" score """
import random
def main():
    # result = convert_score_to_result(float(input("Enter score: ")))
    result = convert_score_to_result(random.randint(0, 100))
    print(f"Your result is: {result}")

def convert_score_to_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()