import sys

"""
Flow Control and Comparators:
1.create a variable and assign to it an expression that is true using the greater than comparator
2.create a variable and assign to it an expression that is false using the greater than comparator
3.create a variable and assign to it an expression that is true using the greater than or equal to comparator
4.create a variable and assign to it an expression that is false using the greater than or equal to comparator
5.create a variable and assign to it an expression that is true using the less than comparator
6.create a variable and assign to it an expression that is false using the less than comparator
7.create a variable and assign to it an expression that is true using the less than or equal to comparator
8.create a variable and assign to it an expression that is false using the less than or equal to comparator
9.create a variable and assign to it an expression that is true using the equal to comparator
10.create a variable and assign to it an expression that is false using the equal to comparator
11.create a variable and assign to it an expression that is true using the not equal to comparator
12.create a variable and assign to it an expression that is false using the not equal to comparator
"""
gtTrue = 1 > 0
gtFalse = 0 > 1
gteTrue = 1 >= 0
gteFalse = 0 >= 1
ltTrue = 0 < 1
ltFalse = 1 < 0
lteTrue = 0 <= 1
lteFalse = 1 <= 0
eqTrue = 0 == 0
eqFalse = 1 == 0
neqTrue = 0 != 1
neqFalse = 0 != 0
# print(gtTrue, gtFalse, gteTrue, gteFalse, ltTrue, ltFalse, lteTrue, lteFalse, eqTrue,
#   eqFalse, neqTrue, neqFalse, sep="\n")

"""
and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator
"""
# type your code for "and, or, and not" below this comment and above the one below it. ---------------------------------
andTrue = True and True
andFalse = True and False
orTrue = True or False
orFalse = False or False
notTrue = not False
notFalse = not True
# print(andTrue, andFalse, orTrue, orFalse, notTrue, notFalse, sep="\n")
# ----------------------------------------------------------------------------------------------------------------------
"""
order of operations for Boolean operators:
1.make var1 evaluate to False by changing or removing a single Boolean operator
2.make var2 evaluate to True by changing or removing a single Boolean operator
"""
# type your code for "order of operations for Boolean operators" below this comment and above the one below it. --------
var1 = not 3 > 1 and 5 != 2 or 6 == 6
# print(f"var1 Before: {var1}")
var1 = not 3 > 1 and 5 != 2 and 6 == 6
# print(f"var1 After: {var1}")
var2 = 4*2 != 6 and not 7 % 6 == 1
# print(f"var2 Before: {var2}")
var2 = 4*2 != 6 or not 7 % 6 == 1
# print(f"var2 After: {var2}")
# ----------------------------------------------------------------------------------------------------------------------

"""
For this problem you are going to make a program that simulates the output of a vending machine that only takes in
coins of American currency.
1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
input number.
    Vending Machine:
    1.water = $1.00
    2.cola = $1.50
    3.gatorade = $2.00
2.After placing an order, the user should be prompted to enter inputs 4 times:
    1.The first time, the user should be prompted to enter the number of quarters they put in the machine. Assign this
    number to a variable as an integer.
    2.The second time, the user should be prompted to enter the number of dimes they put in the machine. Assign this
    number to a variable as an integer.
    3.The third time, the user should be prompted to enter the number of nickles they put in the machine. Assign this
    number to a variable as an integer.
    4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine. Assign this
    number to a variable as an integer.
3.Create a variable to hold the total value of all the coins the user has put into the machine.
4.Use flow control statements to print the user's change or output a message asking the user to try again depending
on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.
New knowledge for this problem:
1.%f format specifier
2.import sys and sys.exit()
3.int()
"""
option = int(input(
    "Which drink do you want? (1 for water [$1.00], 2 for cola [$1.50], 3 for gatorade [$2.00])"))
if option == 1:
    price = 1.0
elif option == 2:
    price = 1.5
elif option == 3:
    price = 2.0
else:
    print("Invalid choice!")
    sys.exit()
numOfQuarters = int(
    input("How many quarters ($0.25) are you putting in the machine?"))
totalValue = numOfQuarters * 0.25
numOfDimes = int(
    input("How many dimes are ($0.10) you putting in the machine? You need {:.2f} more.".format(price-totalValue)))
totalValue += numOfDimes * 0.10
numOfNickles = int(
    input("How many nickles ($0.05) are  you putting in the machine? You need {:.2f} more.".format(price-totalValue)))
totalValue += numOfNickles * 0.05
numOfPennies = int(
    input("How many pennies ($0.01) are you putting in the machine? You need {:.2f} more.".format(price-totalValue)))
totalValue += numOfPennies * 0.01

if totalValue < price:
    print("Not enough money put in. You need ${:.2f} more!".format(
        price-totalValue))
elif totalValue > price:
    print("Here's your change: ${:.2f}".format(totalValue-price))
else:
    print("Exact money!")
