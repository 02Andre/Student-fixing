
sum = 0
number_of_numbers = int(input("How many numbers would you like to sum? "))

print("")
for i in range(number_of_numbers):
    next = int(input("Enter a number: "))
    sum = sum + next

print ("")
print ("Sum: " + str(sum))

total = 0
how_many_tests = int(input("How many test do you need to average? "))

print("")
for i in range(how many tests):
    score = float(input("Enter a score: "))
    total = total + score
average = total / how_many_tests

print("")
print("Average: " + str(round(average, 2)))
print("")
print("The data type of the variable average is..." + str(type(average)))