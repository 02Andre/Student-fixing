
myNumber = 7

print("\nGuess a number between 1 & 10\n")
guess = int(input("Enter a Guess: "))

while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongrats, you guessed my number")
x = 1

while x <= 10:
    print (x)
    x = x + 1
