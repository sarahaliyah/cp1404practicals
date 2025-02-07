"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

MINIMUM_SALES = 0
MAXIMUM_SALES = 1000
MINIMUM_DISCOUNT = 0.1
MAXIMUM_DISCOUNT = 0.15

sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALES:
    if sales < MAXIMUM_SALES:
        bonus = MINIMUM_DISCOUNT
    else:
        bonus = MAXIMUM_DISCOUNT
    print("Bonus = $", int(sales * bonus), sep="")
    sales = float(input("Enter sales: $"))
