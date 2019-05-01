"""
1.Try and Except to handle divide by zero and type errors
a.Use input() to have the user enter two integers as inputs. Assign these to 2 different variables.
b.Define a function that takes two inputs. This function should print the result of the first input divided by the
second input. Use your knowledge of Try and Except statements to print messages for the errors that would occur if
the
second input of the function is 0 or if one or both of the inputs cannot be converted to integers.
c.call the function from step 1.b. with the 2 variables from step 1.a. as inputs.
"""

# NOTE: Only lists, dicts, sets are mutable. Everything else are immutable objects.


def read_input():
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        return num1, num2, True
    except:
        print("Please enter an integer!")
        return False


def divide(num1, num2):
    try:
        res = "{:.2f}".format(num1/num2)
        print(res)
    except ZeroDivisionError:
        print("Cannot divide by zero! Try again.")


result = read_input()
a, b = result[0], result[1]

if result[2]:
    divide(a, b)
