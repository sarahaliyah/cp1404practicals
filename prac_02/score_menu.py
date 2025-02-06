MENU = """(G)et a valid score
(P)rint the result
(S)how stars
(Q)uit"""


def main():
    """display menu and process user's input"""
    score = " "
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Your score is {score}")
        elif choice == "P":
            if score == " ":
                print("Please enter a score!")
            else:
                result = determine_result(score)
                print(f"Your result is {result}")
        elif choice == "S":
            if score == " ":
                print("Please enter a score!")
            else:
                print_asterisks(int(score))
        else:
            print("Invalid Choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye! See you again")


def get_valid_score():
    """get valid score between 0 - 100 inclusive from user"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score please enter again!")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    """determine result based on the score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_asterisks(score):
    """print as many asterisks as the score"""
    print("* " * score)


main()
