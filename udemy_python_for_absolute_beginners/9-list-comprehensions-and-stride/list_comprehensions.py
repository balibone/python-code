"""
1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]
"""
from math import pow
print([num-1 for num in range(9, 0, -2)])
print([int(pow(num, num)) for num in range(1, 5)])

"""
2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]
"""
print([v for v in range(1, 10) if v != 1 and v != 5 and v != 6])
print([v for v in range(10, 0, -1) if v > 7 or v < 4])
print([v for v in range(1, 11) if v != 2 and v != 3 and v != 7 and v != 8])
