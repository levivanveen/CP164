from guesses import guess, character

INPUTS = "0123456789/+*-="
COLOURS = "PG"

i = 0
first_guess = guess()
print("Purple = P, Green = G")
print("If black, press Enter")
print()
print("Enter first guess")

while i < 6:
    inp = input("Enter number/symbol: ")

    while inp not in INPUTS:
        print("Please enter a different number/symbol")
        inp = input("Enter number/symbol: ")
        print()

    colour = input("Enter colour (P, G): ")

    while colour not in COLOURS and colour != "":
        print("Please Enter a different colour")
        colour = input("Enter colour (P, G): ")
        print()

    char = character(inp, colour)
    first_guess.append(char)

    i += 1
