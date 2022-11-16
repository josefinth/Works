from sys import displayhook
import math
import statistics

# Exercise 2: BMI
weight = int(input('Enter you weight ( in kg ):'))
height = float(input('Enter your height (in meter):'))
# Formula: BMI = weight / (height^2)
BMI = weight/math.pow(height, 2)
if BMI <18.5 :
    print('Underweight')
elif 18.5 < BMI < 24.99 :
    print('Normal weight')
elif 25.0 < BMI < 29.99 :
    print('Over weight')
elif BMI > 30.0 :
    print('Obesity')


