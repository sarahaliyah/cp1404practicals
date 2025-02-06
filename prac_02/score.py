"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """get user's score and generate random score then display both results"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    random_result = determine_result(random_score)
    print(random_result)


def determine_result(score):
    """determine result based on the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
