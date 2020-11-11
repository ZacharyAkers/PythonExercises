bill_amount = float(input('Total bill amount? '))
service = input('How was the service? ')
if service == "good":
    total_amount = 1.2 * bill_amount
elif service == "fair":
    total_amount = 1.15 * bill_amount
elif service == "bad":
    total_amount = 1.1 * bill_amount
else:
        print("you left no tip")
print("${:.2f}".format(total_amount))

bill_amount = float(input('Total bill amount? '))
service = input('How was the service? ')
persons = int(input('Split between how many people? '))
if service == "good":
    total_amount = 1.2 * bill_amount
    tip_amount = .2 * bill_amount
    split = total_amount / persons
elif service == "fair":
    total_amount = 1.15 * bill_amount
    tip_amount = .15 * bill_amount
    split = total_amount / persons
elif service == "bad":
    total_amount = 1.1 * bill_amount
    tip_amount = .1 * bill_amount
    split = total_amount / persons
else:
    print("you left no tip")
print("${:.2f}".format(tip_amount))
print("${:.2f}".format(total_amount))
print("${:.2f}".format(split))

height = int(input("Enter the height:"))
width = int(input("Enter the width:"))
gap=" "
def print_rectangle(height, width):
    for i in range(height):
        if i == 0 or i == height-1:
            print(width*'*')
        else: 
            print('*' + gap*(width-2) +'*')   
print_rectangle(height,width)

for i in range(1,6):
    for j in range(6-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

number = int(input("Pick number to get multiples up to 10: "))
for i in range(1,11):
   print(number,'x',i,'=',number*i)