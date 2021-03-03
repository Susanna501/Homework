'''Task1-Write a Python program to calculate a dog's age in human years.
Note: For the first two years, a dog year is equal to 10.5 human years. 
After that,each dog year equals 4 human years.'''

# dog_year = int(input('Year_dog: '))
# human_year = ""
# if dog_year < 0:
# 	print('Incorrect input')
# elif dog_year < 3 and dog_year > -1:
# 	human_year = dog_year * 5.25
# else:
# 	human_year = 10.5 + (dog_year - 2) * 4
# print(human_year)



'''Task2- Write a Python program to check whether an alphabet is a vowel or consonant'''

# word = input('Some letter:') 
# one_letter = 'a, o, u , i, e, y'
# if word.isalpha():
# 	if word in one_letter:
# 		print('You r right: ')
# 	else:
# 		print('constant:')
# else:
# 	print('please input letter')


'''Task3- Write a Python program to check this year is leap year or no.'''

# year = int(input('Enter the Year: '))

# if year % 400 == 0 or year % 4 == 0:
# 	if year % 100 != 0:
# 		print("Leap Year", year)
# 	else:
# 		print('Normal Year', year)
# else:
# 	print('Normal Year', year)


'''version 2'''
# year = int(input('Enter the Year: '))

# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
# 	print("Leap Year", year)
# else:
# 	print('Normal Year', year)


'''Task4- Write a Python program to check if your number is odd or even.'''

# my_number = int(input('My number: '))
# if my_number % 2 == 1:
# 	print('Your number is odd')
# else:
# 	print('Your number is even')


'''Task5- Write a python program which will say who win in game.
The winner is the one which have 2 point.You should try to find pc number(0-5):
if find (your point +=1) otherwise (pc point +=1): '''

import random
user = 0
comp = 0
pc = random.randint(0,5)
my_number = int(input('My number: '))

if my_number == pc:
	user +=1
	print('You find', pc)
else:
	comp +=1
	print('You lost your chance', pc)


pc = random.randint(0,5)
my_number = int(input('My number: '))

if my_number == pc:
	user +=1
	print('You find', pc)
else:
	comp +=1
	print('You lost your chance', pc)
print(user, comp)