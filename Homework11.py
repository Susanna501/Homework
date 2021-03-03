'''Write a Python program to find the smallest number which are
divisible by 12 and 15.'''

# number1 = int(input('My number1: '))
# number2 = int(input('My number2: '))
# end = number1 * number2 + 1
# count = 0

# if number1 > number2:
# 	start = number1
# else:
# 	start = number2

# for i in range(start,end):
# 	count +=1
# 	if i % number1 == 0 and i % number2 == 0:
# 		print('my smallest divisible',i,'Count', count)
# 		break



'''Write a Python program to count the number of even and odd
numbers from a series of numbers(1-100).'''

# num = int(input('My number: '))
# end = num + 1
# count_even = 0
# count_odd = 0

# for i in range(1,end):
# 	if i % 2 == 0:
# 		count_even += 1
# 	else:
# 		count_odd +=1
# print('even',count_even, 'odd',count_odd)

'''version2'''

# num = int(input('My number: '))
# if num % 2 == 0:
# 	count_even = count_odd = num/2
# else:
# 	count_even = num //2
# 	count_odd = num//2 + 1

# print('even',count_even, 'odd',count_odd)



'''Write a Python program that accepts a string and calculate
the number of digits and letters.
string = ‘python 3.9’'''

# string = 'python 3.9'
# count_letter = 0
# count_digit = 0

# for i in string:
# 	if i.isalpha():
# 		count_letter += 1
# 	elif i.isdigit():
# 		count_digit += 1
# print('letter', count_letter, 'digits', count_digit)


'''Write a Python program which have number (73421):
You should calculate (7 + 3 + 4 ….):'''

# my_number = int(input('my_number: '))
# count = 0

# for i in str(my_number):
# 	count += int(i)

# print('calculate',count)


'''Write a loop to find the factorial of any number. You have one input.'''

# num = int(input('my_number: '))
# count = 1
# end = num + 1

# for i in range(2,end):
# 	count *= i
# 	print(i, count)


'''Task7. Check-
Write a python program to check if user age in (18-20) and if sex is male.'''

# user_age = int(input('age: '))
# user_sex = input('sex: ')

# if user_age >= 18 and user_age <= 20 and user_sex.lower() == 'male':
# 	print('your user is correct')

# else:
# 	print('your user is incorrect')


'''Task3. Fibonacci
Write a Python program to get the Fibonacci series between 0
to 40: Fib_num = 0,1,1,2,3,5,8 …..'''

# fib_num = int(input('my number: '))
# num1 = 0
# num2 = 1

# if fib_num <= num1:
# 	print(num1)
# else:
# 	print(num1, num2, end= " ")

# 	for i in range(1, fib_num):	
# 		nextstep = num1 + num2
# 		num1 = num2
# 		num2 = nextstep
# 		print(nextstep, end = " " )


'''version 2'''
# x = 0
# y = 1
# while x < 40:
# 	print(x, end=' ')
# 	x,y = y,x+y




# ''' Task8 - Penalty, Speed Limit'''

# x = int(input('Enter speed: '))
# sp_limit = 50
# penalty = (x - sp_limit) * 1000

# if x <= 50:
#     print('ok')
# elif x <= 100 and sp_limit < penalty:
#     print('Penalty', penalty, 'AMD')
# else:
#     print('License suspended')





from random import randint as r
point = 0
question = input('Do you want play 1st? Y/N: ').upper() == 'Y'

if question:

	while True:

		while True:
			user = input('123: ')
			if user.isdigit():
				user = int(user)
				if 0 < user < 4:
					break
				else:
					print('please input between 1-3')
			else:
				print('please input number ')
				
		print('User Sus',point, '+', user,'=', point + user )
		
		point += user
		res = point >= 21

		if point > 4:
			pc = 4 - point % 4
		else:
			pc = 4- point

		if res:
			print('pc win')
			break
		print('Pc',point, '+', pc,'=', point + pc )
								
		point += pc
		if res:
			print('user win')
			break
else:

	while True:

		if point % 4 == 0:
			pc = r(1,3)

		else:
			pc = 4 - point % 4
		print('Pc',point, '+', pc,'=', point + pc )		

		point += pc
		res = point >= 21
		
		if res:
			print('user win')
			break
		
		if point > 18:
			end = 22- point

		else:
			end = 4

		while True:
			user = input('123: ')
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					break
				else:
					print('please input correct')
			else:
				print('please input number ')

		print('User Sus',point, '+', user,'=', point + user )
		
		point += user
		res = point >= 21
		if res:
			print('pc win')
			break


