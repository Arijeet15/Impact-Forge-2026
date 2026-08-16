import time
import random
import pyttsx3
from config import explain, handle_error
import sys


engine = pyttsx3.init() #tts engine initialization

#Functions
def ask(question):
    """
    This function is similar to Scratch's "ask and wait" block.
    It takes input from the user using Python's input() function. To keep things
    simple for the programmer, it automatically handles the data type for numbers
    and text, unlike Python's built-in input() function. This allows the programmer
    to focus on transitioning from block-based coding to real-world programming
    without worrying about these details, which they will learn later.

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
    This function is similar to Scratch's "repeat" block.
    It takes the number of times to repeat and a function to call as arguments,
    then calls that function the specified number of times. It is designed to
    help programmers avoid getting confused by the syntax of Python's for loops
    so they can focus on the logic of their program.

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
    This function is similar to Scratch's "forever" block.
    It takes a function and calls it repeatedly in an infinite loop using
    Python's while loop.

    Example:
    >>> def say_hello():
    ...     print("Hello!")
    >>> forever(say_hello)
    Hello!
    Hello!
    Hello!
    ... (continues indefinitely)
    """
    while True:
        action(*args, **kwargs)

def wait(seconds):
    """
    This function is similar to Scratch's "wait" block.
    It takes a number of seconds and pauses the program for that amount of
    time.

    Example:
    >>> wait(2)
    (waits for 2 seconds)
    """
    time.sleep(seconds)

def say(text):
    """
    This function is similar to Python's print() function, but instead of
    displaying the text, it speaks the text aloud using text-to-speech.
    If an error occurs while converting the text to speech, it displays
    a simple error message.

    Example:
    >>> say("Hello, World!")
    (speaks "Hello, World!" using text-to-speech)
    """
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        print("Something went wrong while converting text to speech.")

def random_number(start, end):
    """
    This function generates a random whole number between the start and end
    values, including both.

    Example:
    >>> random_number(1, 10)
    5
    """
    return random.randint(start, end)

#Error handeling
_original_excepthook = sys.excepthook

def _excepthook(exc_type, exc_value, exc_traceback):
    try:
        handle_error(exc_type, exc_value, exc_traceback)
    except Exception as e:
        print("An Error Occurred!")
        print("Error can't be explained at this moment because of the reason below:")
        print(e)

sys.excepthook = _excepthook
