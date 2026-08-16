from beyondblocks.core import *

# PART 1 — TypeError
"""
print("Watch young sheldon")
wait("missy")  # This line will raise a TypeError because the argument is not a number. Btw missy is sheldons sister.
print("Let us see how the ai works")
"""
"""Output: 
Watch young sheldon
An Error Occurred! Explanation of the error:
This error means that the program is trying to use a string (a piece of text) in a place where it expects a number. 

It likely happened because a function that requires a number, such as `repeat`, `wait`, or `random_number`, was given a string instead. For example, if you passed a string to the `times` argument in the `repeat` function or to the `seconds` argument in the `wait` function, you would get this error.

To fix this, you should look at the values you're passing to functions that expect numbers and make sure they are actually numbers, not strings. Check if you need to convert any strings to numbers or if you're using the correct variables."""
# Sucessfully handled the TypeError and provided an explanation of the error.

# PART 2 — ValueError
#raise ValueError("Did you watched young sheldon? I am in season 2 rn.")
"""
Output:
An Error Occurred! Explanation of the error:
This error is a "ValueError", which means that the program tried to use a value in a way that is not allowed. 

It's likely that this error occurred because the program was expecting a specific type of input or value, but it received something different instead. However, the error message 'Did you watched young sheldon? I am in season 2 rn.' doesn't seem to be related to the code, so it's unclear what exactly caused the error.

A useful conceptual hint is to look at the parts of the code where user input is being used or where values are being passed to functions, and make sure that the types of these values are what the functions are expecting. Check if there are any places where the code is trying to use a value in a way that might cause a "ValueError". 
"""# Poor AI Model thinking that python interpreter sttarted watching young sheldon. Nevermind the function did its job and provided a useful explanation of the error(as much as he could coz how llama 3 can debug a error saying watch young sheldon 😭)
#TLDR: Sucessfull(Its a good thing that the ai model didnt halucinate and said what it could.)

# I noticed one more thing, that rn the ai is explaining the things well, but many times the user may be curious about the error type and message. So i changed the codes of config.py and main.py to print the error type and message along with the explanation of the error. I think this will be helpful for the user to understand the error better.

# PART 3 - NameError
"""
a = "This is a sentence"
print(type(b))
"""
"""
Output:
An Error Occurred!
Error Type: NameError
Error Message: name 'b' is not defined

Explanation of the error:
The error means that the program tried to use something called 'b', but it doesn't know what 'b' is. 

This error likely happened because the program is trying to use a variable named 'b' before it has been given a value or defined. 

Look at your code to see where you're trying to use 'b' and think about where you should define it, or what value you should give it, before trying to use it.
""" # Sucessfully handled the NameError and provided an explanation of the error.

# PART 4 — ZeroDivisionError
""""
a= 67          #Sixxxx - Seveennnnnnnnnn
b = 0           
print(a/b)    #This will cause a ZeroDivisionError
"""
#Sucessfully handled the ZeroDivisionError and provided an explanation of the error:
"""
Output:
An Error Occurred!
Error Type: ZeroDivisionError
Error Message: division by zero

Explanation of the error:
It looks like your program encountered a "ZeroDivisionError", which means it tried to divide a number by zero. 

This error likely happened because somewhere in your code, you're using a division operation (/) where the divisor (the number you're dividing by) is zero. In division, the divisor cannot be zero, as it's undefined in mathematics.

Take a closer look at your division operations and make sure the divisor is never zero. You might need to add checks to ensure that you're not dividing by zero before performing the division. Think about what your program should do when the divisor could potentially be zero.
"""

#PART 5 — IndexError
"""a = ["Sheldon", "Marry", "Missy", "Georgie", "George", "Meemaw"]
print(a[23])"""

"""
Output:
An Error Occurred!
Error Type: IndexError
Error Message: list index out of range

Explanation of the error:
The error message "IndexError: list index out of range" means that your program is trying to access an item in a list that doesn't exist. 

This error likely occurred because you're trying to access an index in a list that is greater than or equal to the length of the list. For example, if you have a list with 5 items, the valid indices are 0, 1, 2, 3, and 4. If you try to access index 5 or higher, you'll get this error.

Take a look at where you're using lists in your code and check that the indices you're trying to access are within the valid range for that list. Make sure to consider the length of the list and the indices you're trying to access to resolve this issue.
""" #Sucessfull here as well

# PART 6 — KeyError
"""
screenTime = {"Me": 8, "My friend": 2, "My another friend": 0.63}
print(screenTime["My best friend"])
"""
"""
Output:
An Error Occurred!
Error Type: KeyError
Error Message: 'My best friend'

Explanation of the error:
It looks like a runtime error occurred in your Python program. The error is called a KeyError, which means that the program tried to access a value using a key that doesn't exist.

The error message "'My best friend'" suggests that the program was trying to use the string "My best friend" as a key to access a value, but it couldn't find it. This might have happened because you're trying to access a value in a dictionary (a collection of key-value pairs) using a key that doesn't exist in the dictionary.

To figure out what's going on, you should take a look at the part of your code where you're trying to access the value using the key "My best friend". Check if the key is supposed to be there and if it's spelled correctly. Also, think about how you're creating and using your dictionary, and make sure that the key is being added to the dictionary before you try to access it.
"""# Sucessfull here as wwell i guess

# PART 7 — AttributeError
"""
class Dog:
    def bark(self):
        print("Woof!")
        
my_dog = Dog()
my_dog.meow()  # This will raise an AttributeError because the Dog class doesn't
"""
"""
Output:
An Error Occurred!
Error Type: AttributeError
Error Message: 'Dog' object has no attribute 'meow'

Explanation of the error:
It looks like you've encountered an error. The error message says there's an "AttributeError", which means that your code is trying to access something that doesn't exist.

The error seems to have happened because you're trying to make a "Dog" object do something called "meow", but dogs don't meow - cats do. This suggests that the issue is likely with a line of code where you're trying to use the "meow" attribute on a "Dog" object.

Take a look at where you define your "Dog" object and its actions. You might want to check if you've accidentally used a cat's action on a dog, or if you need to create a "Cat" object instead. Think about what actions are typical for dogs and make sure your code matches those actions.
"""# I will say this is good explanation, but it did got a bit drifted and said like dogs dont meow, cats do which is unrelated to the code. I think the explanation should have been more focused on the error and how to fix it rather than bringing in unrelated information about dogs and cats. But overall, it did explain the error type and message well.

#PART 9 — FileNotFoundError
"""
with open("non_existent_file.txt", "r") as file:
    content = file.read()
    """
"""
Output:
An Error Occurred!
Error Type: FileNotFoundError
Error Message: [Errno 2] No such file or directory: 'non_existent_file.txt'

Explanation of the error:
The error means that the program is trying to access a file that doesn't exist. 

It's likely that the error occurred because the program is trying to open or read a file named 'non_existent_file.txt', but this file doesn't exist in the location where the program is looking for it.

Consider checking the file name and path to make sure they are correct, and that the file actually exists in that location. Look at the part of your code that deals with files and file paths to see if there's a mistake or a missing file.
"""# I will call this a sucessfull explanation of the error. It explained the error type and message well, and also provided a useful hint on how to fix it.

#PART 10 — ModuleNotFoundError
# from redbull_racing import max_verstappen
"""
Output:
An Error Occurred!
Error Type: ModuleNotFoundError
Error Message: No module named 'redbull_racing'

Explanation of the error:
The error means that Python cannot find a module named 'redbull_racing' that your program is trying to use. 

This likely happened because your program is trying to import the 'redbull_racing' module, but it does not exist or is not installed in your Python environment.

You should look at the import statements in your code to see where 'redbull_racing' is being imported, and then check if it's a valid module that you need for your program.
"""#It was really good, sucess

#PART 11 — RuntimeError
# raise RuntimeError("Run time error means the error which happens when a athletic sprinter runs too fast and his body cant handle the speed and he gets injured. Just kidding, it means the error which happens when a function is called at an inappropriate time.")
"""
Output:
An Error Occurred!
Error Type: RuntimeError
Error Message: Run time error means the error which happens when a athletic sprinter runs too fast and his body cant handle the speed and he gets injured. Just kidding, it means the error which happens when a function is called at an inappropriate time.

Explanation of the error:
It seems like you've encountered a RuntimeError. This error means that something went wrong while your program was running, but it's not because of a problem with the way the code is written (like a typo). Instead, it's because something unexpected happened when a function was called.

The error message is trying to be a bit humorous, but it's actually pointing to a real issue: a function was called at a time when it shouldn't have been. This could be because the function is being used in a way that doesn't make sense in that particular situation, or because some other part of the code is interfering with it.

To fix this, take a closer look at where the error is happening and think about what functions are being called at that point. Ask yourself: is this function being used at the right time, and with the right inputs? Are there any other parts of the code that might be affecting how this function works? Looking at the order of events and the flow of your program might help you figure out what's going wrong.
"""

#PART 12 — OverflowError
# raise OverflowError()
"""
Output:
An Error Occurred!
Error Type: OverflowError
Error Message: 

Explanation of the error:
This error means that a calculation in your program has resulted in a number that is too large for the computer to handle.

It's likely that this error was caused by a function or operation in your code that keeps increasing a value without stopping, such as a loop that runs too many times or a recursive function that doesn't have a proper stopping condition.

Take a closer look at any loops or recursive functions in your code, especially those that involve multiplication or addition, and think about how you can add a limit or a stopping condition to prevent the calculation from getting too large.
"""# Yup, good one, sucessful

# PART 13 — User-caught error
"""
try:
    raise ValueError("I am a massive terrible-looking error, no one can catch me")
except ValueError as e:
    print("I am a smart user, i caught you terrible error.")
    """
#Here the handel_error function will not be called because the error has been caught and handled by the user.
# Output: I am a smart user, i caught you terrible error.

## Listen, listen, if anyone other then me(arijeet) is reading this, it could be the judges of the hackathon, maybe someone who saw this in github etc etc and you are thinking why this stupid guy is manually writting everything, he can just use loops. Then you are kinda right, i could have used loops but it came in my mind after i was alreday near the end of this file, so i just wrote it manually.
#PS: i know the the file is very messy, and so are my other test files, so i will keep it in my mind from next time.

#Btw results now:
# TEST SUCCESSFUL(spelling can be wrong, not just the spelling, but also the grammar, punctuation, and everything else that too not just here but in the whole project, but dont worry, its only in the test or rough work files, not in the main files.)
