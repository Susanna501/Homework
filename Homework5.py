''' Task1. Write a python program which will check is your number equal the random
number of computer (1-10) if yes print True otherwise False.'''
import random
import calendar

x = int(input('my number: '))
y = random.randint(1,10)
print('my num',x,'random',y)
print('my number', x == y)



'''Task2. Write a python program which will check is your number great or equal
the random number of computer (10-100)if yes print True otherwise False.'''
x = int(input('my number: '))
y = random.randint(10,100)
print('my num',x,'random',y)
print('my number', x >= y)



'''Task3- Write a python program which will show your birthday using calendar.'''
y = int(input('Input the year: '))
m = int(input('Input the month: '))
d = int(input('Input the day: '))
print(calendar.month(y,m))
print('Birthday: ',d)




'''Task4- Write a python program where we use sqrt (definition discriminant):'''
from math import sqrt, pi
a = 60
b = 100
c = -10
D = b**2 - 4 * a * c
x1 = (-b + sqrt(D))/(2 * a)
x2 = (-b - sqrt(D))/(2 * a)
print(x1,x2)	



'''Task5- Write a python program where we use pi (calculate the area of circle)
you have one input (radius circle).'''
r = int(input('radius:')) # c = 2pr
c = 2 * pi * r
print(c)


