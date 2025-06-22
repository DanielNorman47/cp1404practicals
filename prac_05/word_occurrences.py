"""
CP1404 - Intermediate Exercise
Count word occurrences
Estimate: 15m
Actual: 9.5m
"""


def main():
    """Print a list of words and their occurrences from a user given sentence"""
    text = input("Text: ")
    words = text.split()  # split user text into list of words
    words_to_occurrences = {}
    for word in words:
        try:  # for each word, add 1 to counter
            words_to_occurrences[word] += 1
        except KeyError:  # if unique start a counter
            words_to_occurrences[word] = 1

    for word, occurrences in words_to_occurrences.items():
        print(f"{word} : {occurrences}")  # print all words


main()
