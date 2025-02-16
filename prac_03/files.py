# question 1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# question 2
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")

# question 3
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
    print(result)

# question 4
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)
