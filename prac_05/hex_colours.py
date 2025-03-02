COLOUR_CODES = {"amethyst": "#9966cc",
                "boysenberry": "#873260",
                "absolute zero": "#0048ba",
                "cadmiumgreen": "#006b3c",
                "beige": "#f5f5dc",
                "candyapplered": "#ff0800",
                "electricblue": "#7df9ff",
                "mindaro": "#e3f988",
                "blue bell": "#a2a2d0",
                "bright lilac": "#d891ef"}


colour_name = input("Enter a colour name: ").lower()

while colour_name != "":
    hex_code = COLOUR_CODES.get(colour_name)
    if hex_code:
        print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    else:
        print("Invalid colour, please try again.")
    colour_name = input("Enter a colour name: ").lower()

print("Goodbye!")
