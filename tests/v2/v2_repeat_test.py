from main import repeat

# Part 1: Testing repeat function with different inputs for 'times' parameter and checking if the output is as expected:

"""
times_values = [0, 1, 2, 3, 10, 100, -1, -5, -100, 2.5, -2.5, "5", "hello", "", None, True, False, 1+2j, [1, 2, 3], {"times": 5}, float("inf"), float("nan")]

def greet():
    print("Hello!")

for times in times_values:
    print(f"Testing with times = {times}")
    try:
        repeat(times, greet)
    except Exception as e:
        print(f"Error: {e}")
"""#Commented this so that i can now move to the nextpart of testing this function.

#1st Try - Test Failed: The repeat function should raise a ValueError for negative integers, but it did that for negative floats as well. The function should only raise ValueError for negative integers, not for negative floats or other types.
#Fix - Modify the function to check for integer type before checking if it's negative.

"""
Terminal Output:

Testing with times = 0
Testing with times = 1
Hello!
Testing with times = 2
Hello!
Hello!
Testing with times = 3
Hello!
Hello!
Hello!
Testing with times = 10
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Testing with times = 100
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Testing with times = -1
Error: times cannot be negative
Testing with times = -5
Error: times cannot be negative
Testing with times = -100
Error: times cannot be negative
Testing with times = 2.5
Error: 'float' object cannot be interpreted as an integer
Testing with times = -2.5
Error: times cannot be negative
Testing with times = 5
Error: '<' not supported between instances of 'str' and 'int'
Testing with times = hello
Error: '<' not supported between instances of 'str' and 'int'
Testing with times = 
Error: '<' not supported between instances of 'str' and 'int'
Testing with times = None
Error: '<' not supported between instances of 'NoneType' and 'int'
Testing with times = True
Hello!
Testing with times = False
Testing with times = (1+2j)
Error: '<' not supported between instances of 'complex' and 'int'
Testing with times = [1, 2, 3]
Error: '<' not supported between instances of 'list' and 'int'
Testing with times = {'times': 5}
Error: '<' not supported between instances of 'dict' and 'int'
Testing with times = inf
Error: 'float' object cannot be interpreted as an integer
Testing with times = nan
Error: 'float' object cannot be interpreted as an integer
"""

#2nd Try - Test Passed: The repeat function now correctly raises a ValueError for negative integers, while allowing other types to be processed without raising an error. The function now checks for integer type before checking if it's negative, ensuring that only negative integers raise a ValueError.
"""
Terminal Output:

Testing with times = 0
Testing with times = 1
Hello!
Testing with times = 2
Hello!
Hello!
Testing with times = 3
Hello!
Hello!
Hello!
Testing with times = 10
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Testing with times = 100
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Testing with times = -1
Error: times argument cannot be negative
Testing with times = -5
Error: times argument cannot be negative
Testing with times = -100
Error: times argument cannot be negative
Testing with times = 2.5
Error: 'float' object cannot be interpreted as an integer
Testing with times = -2.5
Error: 'float' object cannot be interpreted as an integer
Testing with times = 5
Error: 'str' object cannot be interpreted as an integer
Testing with times = hello
Error: 'str' object cannot be interpreted as an integer
Testing with times = 
Error: 'str' object cannot be interpreted as an integer
Testing with times = None
Error: 'NoneType' object cannot be interpreted as an integer
Testing with times = True
Hello!
Testing with times = False
Testing with times = (1+2j)
Error: 'complex' object cannot be interpreted as an integer
Testing with times = [1, 2, 3]
Error: 'list' object cannot be interpreted as an integer
Testing with times = {'times': 5}
Error: 'dict' object cannot be interpreted as an integer
Testing with times = inf
Error: 'float' object cannot be interpreted as an integer
Testing with times = nan
Error: 'float' object cannot be interpreted as an integer
"""

# Part 2: Testing repeat function with different inputs for 'action' parameter and checking if the output is as expected: [Passed in 1st try]

"""
def simple_function():              # Functions for action parameter testing
    print("Hello!")
def another_function():
    print("Another function!")
def returns_value():
    return 42
def does_nothing():
    pass
def raises_error():
    raise ValueError("Test error")
def takes_argument(x):
    print(x)

action_values = [simple_function, another_function, returns_value, does_nothing, raises_error, None, 5, 2.5, True, False, "hello", "", [], [1, 2, 3], {}, {"action": "test"}, (1, 2)]

for action in action_values:
    print(f"Testing with action = {action!r}")

    try:
        repeat(1, action)
        print("Completed without error")

    except Exception as e:
        print(f"Error: {e}")
"""  #Commented this so that i can now move to the nextpart of testing this function.

"""
Terminal Output:

Testing with action = <function simple_function at 0x0000018759288460>
Hello!
Completed without error
Testing with action = <function another_function at 0x000001875928B5E0>
Another function!
Completed without error
Testing with action = <function returns_value at 0x000001875D660250>
Completed without error
Testing with action = <function does_nothing at 0x000001875D660300>
Completed without error
Testing with action = <function raises_error at 0x000001875D6603B0>
Error: Test error
Testing with action = None
Error: 'NoneType' object is not callable
Testing with action = 5
Error: 'int' object is not callable
Testing with action = 2.5
Error: 'float' object is not callable
Testing with action = True
Error: 'bool' object is not callable
Testing with action = False
Error: 'bool' object is not callable
Testing with action = 'hello'
Error: 'str' object is not callable
Testing with action = ''
Error: 'str' object is not callable
Testing with action = []
Error: 'list' object is not callable
Testing with action = [1, 2, 3]
Error: 'list' object is not callable
Testing with action = {}
Error: 'dict' object is not callable
Testing with action = {'action': 'test'}
Error: 'dict' object is not callable
Testing with action = (1, 2)
Error: 'tuple' object is not callable
"""
