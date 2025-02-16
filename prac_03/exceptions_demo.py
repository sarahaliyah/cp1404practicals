"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Question

When will a ValueError occur?
Answer: When the input of numerator or denominator is not numbers.

When will a ZeroDivisionError occur?
Answer: When the denominator input is 0.

Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes, by adding while loop to validate / error check the number.
"""