'''Write a Python program to check if pc number is great than 10. 
random(1,20) when True break.'''

# import random

# while True:
# 	pc = random.randint(1,20)
# 	n = 10

# 	if n < pc:
# 		break
# 		print('True:',pc)
	
# 	else:
# 		print('False: ',pc)




'''Chinga Chung'''
import random
count_pc = 0
count_user = 0

while True: 
	r ='RPS'
	user = input('please select this character(RPS)')
	pc = random.choice(r)

	if user == 'R' and pc =='S' or user == 'P' and pc == 'R' or user == 'S' and pc == 'P':
		count_user += 1
		print('Good user',pc,'user', user, 'count', count_user)
	
	elif pc == 'R' and user =='S' or pc == 'P' and user == 'R' or pc == 'S' and user == 'P':
		count_pc += 1
		print('Good pc',pc,'user', user, 'count', count_pc)

	else:
		print('no one pc',pc,'user', user, 'count')

	if count_user == 3:
		print('win user count-', count_user)
		break

	elif count_pc == 3:
		print('win pc count-', count_pc)	
		break	










