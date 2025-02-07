total = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(1, number_of_items + 1):
    price = float(input(f"Enter price of item {i}: $"))
    while price < 0:
        print("Invalid price")
        price = float(input(f"Enter price of item {i}: $"))
    total += price

if total > DISCOUNT_THRESHOLD:
    total *= DISCOUNT_RATE

print(f"The total price of {number_of_items} items is $ {total:.2f}")
