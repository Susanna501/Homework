'''1.Create 5 file (.txt) and write messages in them.'''

# with open('MyAccount1.txt','w') as f:
# 	res = 'Hello everyone, where are you from?'
# 	f.write(res)

# with open('MyAccount1.txt') as f:
# 	print(f.read())


# with open('MyAccount2.txt','w') as f:
# 	res = 'Hello everyone, welcome to MyAccount2 file?\n This file for testing'
# 	f.write(res)

# with open('MyAccount2.txt') as f:
# 	print(f.read())


# with open('MyAccount3.txt','w') as f:
# 	res = 'Hello everyone, welcome to MyAccount2 file?\nThis file for testing\nYou can choose your question and tell as'
# 	f.write(res)

# with open('MyAccount3.txt') as f:
# 	print(f.read())


# with open('MyAccount4.txt','w') as f:
# 	res = 'Hello everyone, welcome to MyAccount2 file?\nThis file for testing\nYou can choose your question and tell as'
# 	res1 = '\nInput your login and password'
# 	f.write(res)
# 	f.write(res1)

# with open('MyAccount4.txt') as f:
# 	print(f.read())


# with open('MyAccount5.txt','w') as f:
# 	res = 'Hello everyone, welcome to MyAccount2 file?\nThis file for testing\nYou can choose your question and tell as'
# 	res1 = '\nInput your login and password\nContinue your registration'
# 	f.write(res)
# 	f.write(res1)

# with open('MyAccount5.txt') as f:
# 	print(f.read())




'''2. Write a Python program to read first n lines of a file.'''

# n = 2
# with open('Finance1.txt','a') as f:
# 	res = 'Hello everyone,welcome to MyAccount2 file? This file for testing,You can choose your question and tell as'
# 	f.write(res)
# with open('Finance1.txt') as f:
# 	for i in range(n):
# 		res = f.readline()
# 		print(res)





'''3.Write a Python program to append text to a file and display the text.'''

# f = open('MyAccount5.txt','a')
# res = '\nWrite your ID number, passport number and bank account'
# f.write(res)

# with open('MyAccount5.txt') as f:
# 	print(f.read())



'''4.Write a python program to find the longest words.'''

# with open('MyAccount6.txt','w') as f:
# 	res = 'Hello everyone, welcome to MyAccount6 file? This file for testing wher You canchooseyourquestion and tell as'
# 	f.write(res)

# with open('MyAccount6.txt') as f:
# 	# print(f.read())
# 	res = f.read().split(' ')
# 	print(res)
# 	count = 0
# 	for i in res:
# 		if len(i) > count:
# 			count = len(i)
# 			c = i
# 	print(c)





'''5.Write a python program to find numbers in txt.'''

# with open('MyAccount7.txt','w') as f:
# 	res = 'Hello everyone, welcome to MyAccount7 file# 0771 ? This 07 file for testing num 69534'
# 	f.write(res)

# with open('MyAccount7.txt') as f:
# 	count = []
# 	for i in res.split():
# 		if i.isdigit():
# 			count.append(int(i))
# 		else:
# 			pass
# 	print(count)		




'''6.Write a python program to get login and password.'''

# with open('Account8.txt','w') as f:
# 	login = input('Enter your login: ')
# 	password = input('Enter your pass: ')
# 	f.write('My login is ' + login + 'my password is ' + password)

# with open('Account8.txt') as f:
# 	print(f.read())
