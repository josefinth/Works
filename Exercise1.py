# Exercise 1: DVD Club Points
from sys import displayhook
import math
import statistics

videos_purchased = int(input('Enter the number of videos you purchased:'))
if videos_purchased == 0 :
    print('0')
elif videos_purchased==1 :
    print('5')
elif videos_purchased==2 :
    print('15')
elif videos_purchased==3 :
    print('30')
elif videos_purchased==4 :
    print('60')
else:
    print('Enter a number in the range!')
