"""
0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable
1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input
2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input
3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.
4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
.index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.
"""
intList = [1, 2, 3]
stringList = ["a", "b", "c"]
floatList = [1.1, 2.2, 3.3]


def dummy_return(input):
    return input


print(dummy_return(intList))
print(dummy_return(stringList))
print(dummy_return(floatList))


def return_first_element(input):
    return input[0]


print(return_first_element(intList))
print(return_first_element(stringList))
print(return_first_element(floatList))


def product(input):
    product = 1
    for val in input:
        product *= val
    return product


print(product(intList))


def concat(input):
    return " ".join(input)


print(concat(stringList))


def quotient(input):
    answer, index = 0, 0
    for val in input:
        if index == 0:
            answer = val
        else:
            answer /= val
        index += 1
    return answer


print(quotient(floatList))


def hello_lists(input):
    stringList.append("from hello_lists")
    stringList.index("a")
    stringList.remove("b")
    print(stringList)


hello_lists(stringList)
