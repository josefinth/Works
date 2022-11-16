from sys import displayhook
import math
import statistics

# Exercise 5: Maximum of Two Values

def max_Value(value_A, value_B):
    if isinstance(value_A, int) & isinstance(value_B, int):
        print(max(value_A, value_B))
    else:
        print('Only ineger input is valid!')

# Calling the function max_Value(a,b)
max_Value(4,10)


