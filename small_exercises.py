name = input('What is your name? ')
print("Hello," + name)

name = input('What is your name? ')
length_of_name = len(name)
greeting = "Hello, " + name
counter1 = "your name has "
counter2 = " letters in it! awesome!"
total_counter = counter1 + str(length_of_name) + counter2
print(greeting.upper())
print(total_counter.upper())

print("Please fill in the blanks below:")
print("___(name)___'s favorite subject in school is ___(subject)___")
name = input("What is name? ")
subject = input("What is subject? ")
madlib = name + "'s favorite subject in school is " + subject
print(madlib)

day = int(input('Day (0-6)? '))
if day >= 1:
    if day == 1:
        print("Monday")
    if day == 2:
        print("Tuesday")
    if day == 3:
        print("Wednesday")
    if day == 4:
        print("Thursday")
    if day == 5:
        print("Friday")
    if day == 6:
        print("Saturday")
else:
    print("Sunday")

day = int(input('Day (0-6)? '))
if day > 0 and day < 6:
    print("Go to Work")
else:
    print("Sleep in")

C = int(input('Temperature in C?'))
F = (C * 9/5) + 32
print(F)

count = 1
max = 10
while (count <= max):
    print(count)
    count += 1

count = 2
max = 8
while(count <= max):
    print(count)
    count += 1

side = 5
for i in range(side):
    for i in range(side):
        print('*', end = '')
    print()

side = int(input("How big is the square? "))
for i in range(side):
    for i in range(side):
        print('*', end = '')
    print()
