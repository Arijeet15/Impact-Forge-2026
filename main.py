import time
import random
import pyttsx3
from config import explain, handle_error, handle_error
import sys


engine = pyttsx3.init() #tts engine initialization

#Functions
def ask(question):
    """
    This function is similar to scratch's 'ask' block.
    It takes a input from the user using python input function, but to keep things simple for the programmer handels
    the data type itself for Numbers & Text unlike python's built in input function so that the programmer can focus
    on there transition from block based coding to real world programming without worrying about these minor things
    which they will learn later.

    Example:
    >>> ask("What is your name?")
    What is your name? John
    'John'
    """
    answer = input(question + " ")

    try:
        return int(answer)
    except ValueError:
        try:
            return float(answer)
        except ValueError:
            return answer

def repeat(times, action, /, *args, **kwargs):
    """
    This function is similar to scratch's 'repeat' block.
    It takes a number of times to repeat and a function to call as arguments and calls the function the specified number of times.
    It is there so that the programmer dont gets confused with the syntax of for loops in python and can focus on the logic of the program.

    Example:
    >>> def say_hello():
    ...     print("Hello!")
    >>> repeat(3, say_hello)
    Hello!
    Hello!
    Hello!
    """
    for _ in range(times):
        action(*args, **kwargs)

def forever(action, /, *args, **kwargs):
    """
    This function is similar to scratch's 'forever' block.
    It takes a function, and calls it in a infinite loop using while(True).

    Example:
    >>> def say_hello():
    ...     print("Hello!")
    >>> forever(say_hello)
    Hello!
    Hello!
    Hello!
    ... (infinite times)
    """
    while True:
        action(*args, **kwargs)

def wait(seconds):
    """
    This function is similar to scratch's 'wait' block.
    It takes number of seconds and uses time module's sleep function to wait for that many seconds.

    Example:
    >>> wait(2)
    (waits 2 seconds)
    """
    time.sleep(seconds)

def say(text):
    """
    This function can be used for text to speech.
    It takes a string and uses pyttsx3 module to convert the text to speech.
    It also handles any errors that may occur while converting text to speech.

    Example:
    >>> say("Hello, World!")
    (says "Hello, World!" using text to speech)
    """
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("Something went wrong while converting text to speech.")

def random_number(start, end):
    """
    This function generates a random integer between start and end arguments (inclusive).

    Example:
    >>> random_number(1, 10)
    5
    """
    return random.randint(start, end)

#Error handeling
_original_excepthook = sys.excepthook

def _excepthook(exc_type, exc_value, exc_traceback):
    handle_error(exc_type, exc_value, exc_traceback)

sys.excepthook = _excepthook
