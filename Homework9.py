'''Task1. Values
Take two int values from user and print greatest among them.'''

a = int(input('A value: '))
b = int(input('B value: '))
if a > b:	
	print('a is greater')
elif a == b:
	print('a is equal to b')
else:
	print('b is greater')	



'''Task 2. Age
Take input of age of 3 people by user and determine oldest and youngest among them.'''

people_1 = int(input('1st: ')) 
people_2 = int(input('2nd: ')) 
people_3 = int(input('3rd: ')) 

if people_1 > people_2 and people_1 > people_3:
	print('1st people is oldest')
elif people_2 > people_3 and people_2 > people_1:
	print('2nd people is oldest')
elif people_3 > people_1 and people_3 > people_2:
	print('3rd people is oldest')
else:
	print('All three are equal')	
	


'''Task3. Reverse 
You have number. Write a python program which to print a new number with digits 
reversed as of original one. 
For example:
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895'''

# number = int(input('my number: '))
# first = number % 10
# second = number % 100 // 10
# third = number % 1000 // 100
# forth = number // 1000
# print(int(str(first)+str(second)+str(third)+str(forth)))

# print('1234'[::-1])



'''Task4. Work
Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using
following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR".'''

user_age = int(input('User age: '))
user_sex = input('User sex M or F: ')

if 'female'in user_sex.lower():
	print('She will work only in urban areas')
elif user_age >=20 and user_age < 40 and 'male' in user_sex.lower():
	print('He can work in anywhere')
elif user_age >= 40 and user_age <= 60 and 'male' in user_sex.lower():
	print('He will work in urban areas only.')
else:
	user_age > 61	
	print('ERROR')



'''Task5. Game Rock, Paper, Scissors'''
import random
r = 'RPS'
user = input('please select this character(RPS)')
game = random.choice(r)

if user == 'R' and game == 'P' or user == 'P' and game == 'S' or user == 'S' and game == 'R':
	print('Win pc', game)
elif user == 'R' and game == 'R' or user == 'P' and game == 'P' or user == 'S' and game == 'S':
	print('no one', game)
else:
	print('win user',user)



'''Task6. Instagram
You (input) and pc have followers (pc have random followers) if your followers
is great 20 % than pc you are blogger otherwise pc is blogger.'''

# import random
# num = int(input('my number: '))
# pc = random.randint(1,10)

# if num >= pc + pc * 0.2:
# 	print('You are blogger',num)
# else:
# 	print('pc is blogger', pc)



'''7. Rally
You and the Pc take part in the rally,You must pass 12 km. 
PC passed in 3 minutes and You are 10% later than Pc.how much is the speed of your car.'''

# km = 12
# time = 3 * 0.1 + 3
# user_speed = km/ time
# print(user_speed)


'''Task 8-1'''

# import random
# number = int(input('my number: '))
# pc = random.randint(1,5)

# if number == pc:
# 	print('It is your step', pc)
# elif number >= pc:
# 	number += number* 0.2
# 	print('You win 20 percent and your chance is good', number, 'PC', pc)
# else:	
# 	print('You lost your chance', pc)

'''Task 8-2'''

# account = int(input('my account: '))

# if account == 800000:
# 	tax = account * 0.05
# 	print('your 1st tax is','tax', tax)
# elif account >= 350000 and account<=650000:
# 	tax = account * 0.025
# 	print('your 2nd tax is','tax',tax)
# elif account > 650001 and account <= 800001:
# 	tax = account * 0.01667
# 	print('your 3rd tax is','tax',tax)
# else:
# 	print('You lose your chance')

