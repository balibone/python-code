"""
1.While Loop Basics
a.create a while loop that prints out a string 5 times (should not use a break statement)
b.create a while loop that appends 1, 2, and 3 to an empty string and prints that string
c.print the list you created in step 1.b.
"""
i = 0
while i < 5:
    print("times")
    i += 1

idx, text = 1, ""
while idx <= 3:
    text += str(idx)
    idx += 1
print(text)
"""
2.while/else and break statements
a.create a while loop that does the same thing as the the while loop you created in step 1.a. but uses a break
statement
to end the loop instead of what was used in step 1.a.
b.use the input function to make the user of the program guess your favorite fruit
c.create a while/else loop that continues to prompt the user to guess what your favorite fruit is until they guess
correctly (use the input function for this.) The else should be triggered when the user correctly guesses your
favorite fruit. When the else is triggered, it should output a message saying that the user has correctly guessed
your favorite fruit.
"""
count = 0
while True:
    if count > 4:
        break
    print("haha")
    count += 1

guess_fav = input("Guess my favourite fruit motherfucker!")

actual_fav = "banana"

while guess_fav.strip().casefold() != actual_fav.casefold():
    guess_fav = input("I'm funny how?! Guess again you motherfucker!")
else:
    print("Oh you motherfucker you!")
