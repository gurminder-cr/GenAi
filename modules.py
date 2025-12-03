import random 
# import dict

print(random.randint(1,50)) #Return random integer in range [a, b], including both end points.

a=['pink','red','yellow','green','black','red']
print(a)
print(random.choice(a))
print(random.choices(a,k=2)) #Return a k sized list of population elements chosen with replacement


print("------------------")

import math 
# n=int(input('Enter number '))
# print(math.factorial(n))

print(math.sqrt(120))
print(math.pow(2,5)) #Return x**y (x to the power of y).

print("------------------time----------------")
import time 

print('Hello ')
# time.sleep(5)

print('Hello after 5 seconds')


import datetime 
print(datetime.datetime.today())
print(datetime.date.today())
my_specific_datetime = datetime.datetime(2025, 12, 25, 10, 30, 0)
print(f'Time is {my_specific_datetime}')