"""
string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it
"""
# type your code for "string and escape sequences" in between this single line comment and the one below it ------------
doubleQuoteString = "test"
singleQuoteString = 'test'
doubleQuoteEscapedString = "hello \"test\""
singleQuoteNonEscapedString = "hello 'test'"
singleQuoteEscapedString = 'hello \'test\''
# ----------------------------------------------------------------------------------------------------------------------
"""
accessing values by index and string slicing:
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
2.create a variable and assign it the "a" from the string assigned to the variable lannisters.
3.create a variable and assign it the "J" from the string assigned to the variable lannisters.
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters.
5.create a variable and assign it "Cersei" from the string assigned to the variable lannisters.
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.
"""
# type your code for "accessing values by index and string slicing" in between this comment and the one below it -------
lannisters = "JaimeCerseiTyrion"
lowercaseA = lannisters[1]
capitalJ = lannisters[0]
jaimeName = lannisters[:5]
cerseiName = lannisters[5:11]
tyrionName = lannisters[11:]
myAnswer = "{} {} {} {} {}".format(
    lowercaseA, capitalJ, jaimeName, cerseiName, tyrionName)
realAnswer = "a J Jaime Cersei Tyrion"
print(myAnswer)
print(realAnswer)
print(myAnswer == realAnswer)

# ----------------------------------------------------------------------------------------------------------------------
"""
len() and str() practice:
1.create a variable and assign it the string "Python"
2.create another variable and assign it the length of the string assigned to the variable in step 1
3.create a variable and use string slicing and len() to assign it the length of the slice "yth" from the string assigned
to the variable from step 1
4.create a variable and assign it the float 1.32
5.create a variable and assign it the string "2" from the float assigned to the variable from the last problem (use the
str() string method for this)
"""
# type your code for "len() and str() practice" below this single line comment and above the one below it --------------
languageName = "Python"
length = len(languageName)
subLength = len(languageName[1:4])
floatingNumber = 1.32
stringFloat = str(floatingNumber)[3]
print(length, subLength, floatingNumber, stringFloat)
# ----------------------------------------------------------------------------------------------------------------------
"""
.upper() and .lower() practice:
1.create a variable and assign it the string "upper" changed to "UPPER" using .upper()
2.create a variable and assign it the string "owe" from "LOWER" using string slicing and .lower()
"""
# type your code for ".upper() and .lower() practice" below this single line comment and above the one below it --------
upper = "upper".upper()
lower = "LOWER"[1:4].lower()
print(upper, lower)
# ----------------------------------------------------------------------------------------------------------------------

"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""
# type your code for "String Concatenation" below this comment and above the one below it. -----------------------------
helloWorld = "hello" + " world"
eleven = 11
thirtyEight = 38
elevenThirtyEight = eleven+thirtyEight
# ----------------------------------------------------------------------------------------------------------------------
"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit
[name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""
# type your code for "%s and input()" below this comment and above the one below it. -----------------------------------
favouriteRestaurant = input("What is your favourite restaurant?")
favouritePlace = input("What is a place you want to visit?")
firstName = input("What is your first name?")
sentence = "Your favourite restaurant is {restaurant}, you want to visit {place}, and your nickname or first name is {name}".format(
    restaurant=favouriteRestaurant, place=favouritePlace, name=firstName)
print(sentence)
# ----------------------------------------------------------------------------------------------------------------------
