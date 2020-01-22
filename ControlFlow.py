

myNumber = 7

print("\nGuess a number between 1 & 10\n")
guess = int(input("Enter a Guess: "))
#Programmer:Andre date: 1-22-2020 whileloop

while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongrats, you guessed my number")

print("\n\t***********\n")

x = 1

while x <= 10:
    print (x)
    x = x + 1
    
print("\n\t***********\n")

sum = 0
number_of_numbers = int(input("How many numbers would you like to sum? "))
print("")
for i in range(number_of_numbers):
    next = int(input("Enter a number: "))
    sum = sum + next
#Programmer:Andre date: 1-22-2020 ForLoop
print ("")
print ("Sum: " + str(sum))

total = 0
how_many_tests = int(input("How many test do you need to average? "))

print("\n\t***********\n")

for i in range(how_many_tests):
    score = float(input("Enter a score: "))
    total = total + score
average = total / how_many_tests

print("")
print("Average: " + str(round(average, 2)))
print("")
print("The data type of the variable average is..." + str(type(average)))

