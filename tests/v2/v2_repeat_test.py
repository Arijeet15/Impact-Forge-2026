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

# Part 3: Testing repeat function with different inputs for 'args' - Passed in 1st try
"""
times = 2

def one_arg(x):
    print(f"Got: {x}")
def two_args(x, y):
    print(f"Got: {x}, {y}")
def three_args(x, y, z):
    print(f"Got: {x}, {y}, {z}")
def no_args():
    print("No arguments")
def many_args(a, b, c, d):
    print(f"Got: {a}, {b}, {c}, {d}")

args_tests = [
    (no_args, ()),
    (one_arg, ("hello",)),
    (one_arg, (123,)),
    (one_arg, (None,)),
    (two_args, ("hello", "world")),
    (two_args, (1, 2)),
    (three_args, (1, 2, 3)),
    (many_args, (1, 2, 3, 4)),
    (one_arg, ()),
    (two_args, ("hello",)),
    (two_args, ("hello", "world", "extra")),
    (three_args, (1, 2)),
    (three_args, (1, 2, 3, 4)),
    (many_args, (1, 2, 3)),
]

for action, args in args_tests:
    print(f"\nTesting action={action.__name__}, args={args!r}")

    try:
        repeat(2, action, *args)
        print("Completed without error")

    except Exception as e:
        print(f"Error: {e}")
"""
"""
Terminal Output:

Testing action=no_args, args=()
No arguments
No arguments
Completed without error

Testing action=one_arg, args=('hello',)
Got: hello
Got: hello
Completed without error

Testing action=one_arg, args=(123,)
Got: 123
Got: 123
Completed without error

Testing action=one_arg, args=(None,)
Got: None
Got: None
Completed without error

Testing action=two_args, args=('hello', 'world')
Got: hello, world
Got: hello, world
Completed without error

Testing action=two_args, args=(1, 2)
Got: 1, 2
Got: 1, 2
Completed without error

Testing action=three_args, args=(1, 2, 3)
Got: 1, 2, 3
Got: 1, 2, 3
Completed without error

Testing action=many_args, args=(1, 2, 3, 4)
Got: 1, 2, 3, 4
Got: 1, 2, 3, 4
Completed without error

Testing action=one_arg, args=()
Error: one_arg() missing 1 required positional argument: 'x'

Testing action=two_args, args=('hello',)
Error: two_args() missing 1 required positional argument: 'y'

Testing action=two_args, args=('hello', 'world', 'extra')
Error: two_args() takes 2 positional arguments but 3 were given

Testing action=three_args, args=(1, 2)
Error: three_args() missing 1 required positional argument: 'z'

Testing action=three_args, args=(1, 2, 3, 4)
Error: three_args() takes 3 positional arguments but 4 were given

Testing action=many_args, args=(1, 2, 3)
Error: many_args() missing 1 required positional argument: 'd'
"""

# Part 4: Testing repeat function with different inputs for 'kwargs' - Passed in 1st try
"""
times = 2

def one_kwarg(name):                # Functions for kwargs parameter testing
    print(f"Hello, {name}!")
def two_kwargs(name, greeting):
    print(f"{greeting}, {name}!")
def default_kwargs(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
def multiple_kwargs(name, age, city):
    print(f"{name}, {age}, {city}")
def no_kwargs():
    print("No kwargs")

kwargs_tests = [
    (no_kwargs, {}),
    (one_kwarg, {"name": "Arijeet"}),
    (two_kwargs, {"name": "Arijeet", "greeting": "Hello"}),
    (default_kwargs, {"name": "Arijeet"}),
    (default_kwargs, {"name": "Arijeet", "greeting": "Hi"}),
    (multiple_kwargs, {"name": "Arijeet", "age": 15, "city": "Dalli Rajhara"}),
    (one_kwarg, {}),
    (two_kwargs, {"name": "Arijeet"}),
    (two_kwargs, {"name": "Arijeet", "greeting": "Hi", "extra": "x"}),
    (one_kwarg, {"wrong": "value"}),
    (multiple_kwargs, {"name": "Arijeet", "age": 15}),
]

for action, kwargs in kwargs_tests:
    print(f"\nTesting action={action.__name__}, kwargs={kwargs!r}")

    try:
        repeat(2, action, **kwargs)
        print("Completed without error")

    except Exception as e:
        print(f"Error: {e}")
"""

"""
Terminal Output:

Testing action=no_kwargs, kwargs={}
No kwargs
No kwargs
Completed without error

Testing action=one_kwarg, kwargs={'name': 'Arijeet'}
Hello, Arijeet!
Hello, Arijeet!
Completed without error

Testing action=two_kwargs, kwargs={'name': 'Arijeet', 'greeting': 'Hello'}
Hello, Arijeet!
Hello, Arijeet!
Completed without error

Testing action=default_kwargs, kwargs={'name': 'Arijeet'}
Hello, Arijeet!
Hello, Arijeet!
Completed without error

Testing action=default_kwargs, kwargs={'name': 'Arijeet', 'greeting': 'Hi'}
Hi, Arijeet!
Hi, Arijeet!
Completed without error

Testing action=multiple_kwargs, kwargs={'name': 'Arijeet', 'age': 15, 'city': 'Dalli Rajhara'}
Arijeet, 15, Dalli Rajhara
Arijeet, 15, Dalli Rajhara
Completed without error

Testing action=one_kwarg, kwargs={}
Error: one_kwarg() missing 1 required positional argument: 'name'

Testing action=two_kwargs, kwargs={'name': 'Arijeet'}
Error: two_kwargs() missing 1 required positional argument: 'greeting'

Testing action=two_kwargs, kwargs={'name': 'Arijeet', 'greeting': 'Hi', 'extra': 'x'}
Error: two_kwargs() got an unexpected keyword argument 'extra'

Testing action=one_kwarg, kwargs={'wrong': 'value'}
Error: one_kwarg() got an unexpected keyword argument 'wrong'

Testing action=multiple_kwargs, kwargs={'name': 'Arijeet', 'age': 15}
Error: multiple_kwargs() missing 1 required positional argument: 'city'
"""

# Part 5: Combining them all and testing - Passed in 1st try(Yayyyyyy)
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
def introduce(name, age, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}.")
def calculate(a, b, operation="add"):
    if operation == "add":
        print(a + b)
    elif operation == "multiply":
        print(a * b)

combination_tests = [
    (3, greet, ("Arijeet",), {}),
    (2, greet, ("Arijeet",), {"greeting": "Hi"}),
    (1, introduce, ("Arijeet", 15), {}),
    (3, introduce, ("Arijeet", 15), {"city": "Dalli Rajhara"}),
    (2, calculate, (5, 3), {}),
    (2, calculate, (5, 3), {"operation": "multiply"}),
    (0, greet, ("Arijeet",), {"greeting": "Hi"}),
    (3, greet, (), {"greeting": "Hi"}),
    (3, greet, ("Arijeet", "extra"), {}),
    (3, greet, ("Arijeet",), {"unknown": "x"}),
    (3, introduce, ("Arijeet",), {}),
    (3, calculate, (5,), {})
]

for times, action, args, kwargs in combination_tests:
    print(f"\nTesting times={times}, action={action.__name__}, args={args!r}, kwargs={kwargs!r}")

    try:
        repeat(times, action, *args, **kwargs)
        print("Completed without error")

    except Exception as e:
        print(f"Error: {e}")

"""
Terminal Output:

Testing times=3, action=greet, args=('Arijeet',), kwargs={}
Hello, Arijeet!
Hello, Arijeet!
Hello, Arijeet!
Completed without error

Testing times=2, action=greet, args=('Arijeet',), kwargs={'greeting': 'Hi'}
Hi, Arijeet!
Hi, Arijeet!
Completed without error

Testing times=1, action=introduce, args=('Arijeet', 15), kwargs={}
Arijeet is 15 years old and lives in Unknown.
Completed without error

Testing times=3, action=introduce, args=('Arijeet', 15), kwargs={'city': 'Dalli Rajhara'}
Arijeet is 15 years old and lives in Dalli Rajhara.
Arijeet is 15 years old and lives in Dalli Rajhara.
Arijeet is 15 years old and lives in Dalli Rajhara.
Completed without error

Testing times=2, action=calculate, args=(5, 3), kwargs={}
8
8
Completed without error

Testing times=2, action=calculate, args=(5, 3), kwargs={'operation': 'multiply'}
15
15
Completed without error

Testing times=0, action=greet, args=('Arijeet',), kwargs={'greeting': 'Hi'}
Completed without error

Testing times=3, action=greet, args=(), kwargs={'greeting': 'Hi'}
Error: greet() missing 1 required positional argument: 'name'

Testing times=3, action=greet, args=('Arijeet', 'extra'), kwargs={}
extra, Arijeet!
extra, Arijeet!
extra, Arijeet!
Completed without error

Testing times=3, action=greet, args=('Arijeet',), kwargs={'unknown': 'x'}
Error: greet() got an unexpected keyword argument 'unknown'

Testing times=3, action=introduce, args=('Arijeet',), kwargs={}
Error: introduce() missing 1 required positional argument: 'age'

Testing times=3, action=calculate, args=(5,), kwargs={}
Error: calculate() missing 1 required positional argument: 'b'
"""

# Part 6 - The Endgame
def raises_value_error():
    raise ValueError("Something went wrong]")
# def raises_type_error():
#     raise TypeError("Invalid type")
# def raises_zero_division():
#     return 10 / 0
# def raises_runtime_error():
#     raise RuntimeError("Test runtime error")

error_tests = [
    (1, raises_value_error),
    #(2, raises_type_error),
    #(3, raises_zero_division),
    #(1, raises_runtime_error),      #Commented the other errors so i can test 1 without try/execpt
]

for times, action in error_tests:
    print(f"\nTesting times={times}, action={action.__name__}")

    #try:
    repeat(times, action)
    print("Unexpected: completed without error")   #Oh yessss, it threw error as expected, means test sucessful

    #except Exception as e:
        #print(f"Caught: {type(e).__name__}: {e}")

"""
Terminal Output:

Testing times=3, action=greet, args=('Arijeet',), kwargs={}
Hello, Arijeet!
Hello, Arijeet!
Hello, Arijeet!
Completed without error

Testing times=2, action=greet, args=('Arijeet',), kwargs={'greeting': 'Hi'}
Hi, Arijeet!
Hi, Arijeet!
Completed without error

Testing times=1, action=introduce, args=('Arijeet', 15), kwargs={}
Arijeet is 15 years old and lives in Unknown.
Completed without error

Testing times=3, action=introduce, args=('Arijeet', 15), kwargs={'city': 'Dalli Rajhara'}
Arijeet is 15 years old and lives in Dalli Rajhara.
Arijeet is 15 years old and lives in Dalli Rajhara.
Arijeet is 15 years old and lives in Dalli Rajhara.
Completed without error

Testing times=2, action=calculate, args=(5, 3), kwargs={}
8
8
Completed without error

Testing times=2, action=calculate, args=(5, 3), kwargs={'operation': 'multiply'}
15
15
Completed without error

Testing times=0, action=greet, args=('Arijeet',), kwargs={'greeting': 'Hi'}
Completed without error

Testing times=3, action=greet, args=(), kwargs={'greeting': 'Hi'}
Error: greet() missing 1 required positional argument: 'name'

Testing times=3, action=greet, args=('Arijeet', 'extra'), kwargs={}
extra, Arijeet!
extra, Arijeet!
extra, Arijeet!
Completed without error

Testing times=3, action=greet, args=('Arijeet',), kwargs={'unknown': 'x'}
Error: greet() got an unexpected keyword argument 'unknown'

Testing times=3, action=introduce, args=('Arijeet',), kwargs={}
Error: introduce() missing 1 required positional argument: 'age'

Testing times=3, action=calculate, args=(5,), kwargs={}
Error: calculate() missing 1 required positional argument: 'b'

Testing times=1, action=raises_value_error
Caught: ValueError: Something went wrong

Testing times=2, action=raises_type_error
Caught: TypeError: Invalid type

Testing times=3, action=raises_zero_division
Caught: ZeroDivisionError: division by zero

Testing times=1, action=raises_runtime_error
Caught: RuntimeError: Test runtime error
"""

#hoooo, log process but finally after all the wwork the repeat function is now working as expected, and all the tests have passed successfully.

# TEST SUCESSFUL
