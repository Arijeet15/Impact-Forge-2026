from beyondblocks.core import random_number

random_tests = [
    (1, 10),
    (0, 1),
    (1, 1),
    (0, 0),
    (-10, 10),
    (-5, -1),
    (100, 200),
    (1, 1000000),
    (10, 1),
    (5, 5.5),
    (1.5, 10),
    ("1", 10),
    (1, "10"),
    ("hello", 10),
    ("Max Verstappen", 10),
    (1, "Max Verstappen"),
    ("Max Verstappen", "Lewis Hamilton"),
    (None, 10),
    (1, None),
    (True, 10),
    (1, False),
    (True, False),
    (1 + 2j, 10),
    ([1, 2, 3], 10),
    (1, [1, 2, 3]),
    ({"start": 1}, 10),
    (1, {"end": 10}),
    ([], []),
    (float("inf"), 10),
    (1, float("inf")),
    (float("nan"), 10),
    (1, float("nan")),
    (-1000000, 1000000),
    (-999999999, 999999999),
    (42, 42),
    (3.1415, -3.1415),
    (7, 8),
    (-1, 0),
]

for start, end in random_tests:
    print(f"Testing random_number({start}, {end})")
    try:
        result = random_number(start, end)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

"""
Terminal outputs:

Testing random_number(1, 10)
Result: 8
Testing random_number(0, 1)
Result: 0
Testing random_number(1, 1)
Result: 1
Testing random_number(0, 0)
Result: 0
Testing random_number(-10, 10)
Result: 7
Testing random_number(-5, -1)
Result: -3
Testing random_number(100, 200)
Result: 102
Testing random_number(1, 1000000)
Result: 121751
Testing random_number(10, 1)
Error: empty range in randint(10, 1)
Testing random_number(5, 5.5)
Error: 'float' object cannot be interpreted as an integer
Testing random_number(1.5, 10)
Error: 'float' object cannot be interpreted as an integer
Testing random_number(1, 10)
Error: 'str' object cannot be interpreted as an integer
Testing random_number(1, 10)
Error: 'str' object cannot be interpreted as an integer
Testing random_number(hello, 10)
Error: 'str' object cannot be interpreted as an integer
Testing random_number(Max Verstappen, 10)
Error: 'str' object cannot be interpreted as an integer
Testing random_number(1, Max Verstappen)
Error: 'str' object cannot be interpreted as an integer
Testing random_number(Max Verstappen, Lewis Hamilton)
Error: 'str' object cannot be interpreted as an integer
Testing random_number(None, 10)
Error: 'NoneType' object cannot be interpreted as an integer
Testing random_number(1, None)
Error: 'NoneType' object cannot be interpreted as an integer
Testing random_number(True, 10)
Result: 7
Testing random_number(1, False)
Error: empty range in randint(1, 0)
Testing random_number(True, False)
Error: empty range in randint(1, 0)
Testing random_number((1+2j), 10)
Error: 'complex' object cannot be interpreted as an integer
Testing random_number([1, 2, 3], 10)
Error: 'list' object cannot be interpreted as an integer
Testing random_number(1, [1, 2, 3])
Error: 'list' object cannot be interpreted as an integer
Testing random_number({'start': 1}, 10)
Error: 'dict' object cannot be interpreted as an integer
Testing random_number(1, {'end': 10})
Error: 'dict' object cannot be interpreted as an integer
Testing random_number([], [])
Error: 'list' object cannot be interpreted as an integer
Testing random_number(inf, 10)
Error: 'float' object cannot be interpreted as an integer
Testing random_number(1, inf)
Error: 'float' object cannot be interpreted as an integer
Testing random_number(nan, 10)
Error: 'float' object cannot be interpreted as an integer
Testing random_number(1, nan)
Error: 'float' object cannot be interpreted as an integer
Testing random_number(-1000000, 1000000)
Result: 313210
Testing random_number(-999999999, 999999999)
Result: 310376478
Testing random_number(42, 42)
Result: 42
Testing random_number(3.1415, -3.1415)
Error: 'float' object cannot be interpreted as an integer
Testing random_number(7, 8)
Result: 8
Testing random_number(-1, 0)
Result: 0
"""

# TEST SUCCESSFUL