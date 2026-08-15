# Actual Python:
# import time

# print("Hello, World!")
# time.sleep(1)    
# name = input("What is your name? ")
# age = int(input("What is your age? "))
# time.sleep(1)
# print(f"You are {name} and next year you will be {age+1} years old.")

# My code:
from main import *
code = """
#include <studio.h>
int main(void) {
    printf("Hello, World!");
    return 0;
}
"""

explanation = explain(code)
print(explanation)