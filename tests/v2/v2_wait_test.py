from beyondblocks.core import wait

wait_values = [
    0,
    1,
    2,
    0.1,
    0.5,
    -1,
    -0.5,
    "2",
    "hello",
    None,
    True,
    False,
    1 + 2j,
    [1, 2],
    "Max Verstappen",
    {"key": "value", "number": 42},
    [1,2,3][0]
]

for value in wait_values:
    print(f"Testing wait with seconds = {str(value)}({value})")
    try:
        wait(value)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

"""
Terminal outputs:

Testing wait with seconds = 0(0)
Success
Testing wait with seconds = 1(1)
Success
Testing wait with seconds = 2(2)
Success
Testing wait with seconds = 0.1(0.1)
Success
Testing wait with seconds = 0.5(0.5)
Success
Testing wait with seconds = -1(-1)
Error: sleep length must be non-negative
Testing wait with seconds = -0.5(-0.5)
Error: sleep length must be non-negative
Testing wait with seconds = 2(2)
Error: 'str' object cannot be interpreted as an integer or float
Testing wait with seconds = hello(hello)
Error: 'str' object cannot be interpreted as an integer or float
Testing wait with seconds = None(None)
Error: 'NoneType' object cannot be interpreted as an integer or float
Testing wait with seconds = True(True)
Success
Testing wait with seconds = False(False)
Success
Testing wait with seconds = (1+2j)((1+2j))
Error: 'complex' object cannot be interpreted as an integer or float
Testing wait with seconds = [1, 2]([1, 2])
Error: 'list' object cannot be interpreted as an integer or float
Testing wait with seconds = Max Verstappen(Max Verstappen)
Error: 'str' object cannot be interpreted as an integer or float
Testing wait with seconds = {'key': 'value', 'number': 42}({'key': 'value', 'number': 42})
Error: 'dict' object cannot be interpreted as an integer or float
Testing wait with seconds = 1(1)
Success
"""

# TEST SUCCESSFUL
