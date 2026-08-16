from beyondblocks.core import ask

# Testing different type of inputs and checking if the asigned variable is of the correct data type or not:

test_inputs = ["15", "-15", "15.5", "-15.5", "0", "0.0", "hello", "hello123", "123abc", "", "   ", "00123", "1e15", "+15", "-0", "000.50", "1.5e-3", "inf", "nan", "12.34.56", "hello world", "😭😂", "the quick brown fox jumps over the lazy dog"]
data = {}

def test_ask():
    a = ask("Enter something:")
    data[a] = type(a)
    print(f"Input: {a}, Type: {type(a)}")


for i in range(len(test_inputs)):
    test_ask()

print(data)

"""
Terminal Output:

Enter something: 15
Input: 15, Type: <class 'int'>
Enter something: -15
Input: -15, Type: <class 'int'>
Enter something: 15.5
Input: 15.5, Type: <class 'float'>
Enter something: -15.5
Input: -15.5, Type: <class 'float'>
Enter something: 0
Input: 0, Type: <class 'int'>
Enter something: 0.0
Input: 0.0, Type: <class 'float'>
Enter something: hello
Input: hello, Type: <class 'str'>
Enter something: hello123
Input: hello123, Type: <class 'str'>
Enter something: 123abc
Input: 123abc, Type: <class 'str'>
Enter something: 
Input: , Type: <class 'str'>
Enter something:   
Input:   , Type: <class 'str'>
Enter something: 00123
Input: 123, Type: <class 'int'>
Enter something: 1e15
Input: 1000000000000000.0, Type: <class 'float'>
Enter something: +15
Input: 15, Type: <class 'int'>
Enter something: -0
Input: 0, Type: <class 'int'>
Enter something: 000.50
Input: 0.5, Type: <class 'float'>
Enter something: 1.5e-3
Input: 0.0015, Type: <class 'float'>
Enter something: inf
Input: inf, Type: <class 'float'>
Enter something: nan
Input: nan, Type: <class 'float'>
Enter something: 12.34.56
Input: 12.34.56, Type: <class 'str'>
Enter something: hello world
Input: hello world, Type: <class 'str'>
Enter something: 😭😂
Input: 😭😂, Type: <class 'str'>
Enter something: the quick brown fox jumps over the lazy dog
Input: the quick brown fox jumps over the lazy dog, Type: <class 'str'>
{15: <class 'int'>, -15: <class 'int'>, 15.5: <class 'float'>, -15.5: <class 'float'>, 0: <class 'int'>, 'hello': <class 'str'>, 'hello123': <class 'str'>, '123abc': <class 'str'>, '': <class 'str'>, '  ': <class 'str'>, 123: <class 'int'>, 1000000000000000.0: <class 'float'>, 0.5: <class 'float'>, 0.0015: <class 'float'>, inf: <class 'float'>, nan: <class 'float'>, '12.34.56': <class 'str'>, 'hello world': <class 'str'>, '😭😂': <class 'str'>, 'the quick brown fox jumps over the lazy dog': <class 'str'>}
"""

# TEST SUCESSFUL
