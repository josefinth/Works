from sys import displayhook
import math
import statistics

# Exercise 4: Sum of Numbers
# Find the sum of a serie of positive numbers.

Sum = 0
Positive_number = 0
while True:
    try:
        Positive_number = int(input('Enter enter a series of positive numbers (positive number, to signal end of serie enter a negative number): '))
        print(Positive_number)
        assert Positive_number > 0       # Test if it is positive
        Sum = Sum + Positive_number      # Creates a counter for all positive values entered. 
    except AssertionError :
        print('The sum of the serie is', Sum)
        break
