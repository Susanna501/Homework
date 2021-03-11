
'''Password generator with try except'''

def my_pass():
	
	while True:

		try:
			password = input('Enter your pass: ')
			count = 0
			for i in password:
				if i.isdigit():
					count += 1

			if not password.istitle() and len(password) >= 9 and count > 1:
				raise TypeError ('Only upper letter')
				return 'Thanks for registration'
		
			else:
				return 'Your password not Valid'
		
		except ValueError:
			print('Not Valid pass')
		
		except TypeError:
			print('Valid pass')
			break

print(my_pass( ))




'''Calculator'''

def calculator():
	while True:

		global num1,num2

		try:
			num1 = input('enter your 1st number: ')
			num2 = input('enter your 2nd number: ')

			if num1.isdigit() and num2.isdigit():
				num1,num2 = int(num1),int(num2)
				raise TypeError ('Only numbers')
				return "It's ok"
			
			else:
				return 'Please input only numbers'
				break

		except ValueError:
			print('need numbers only')
		
		except TypeError:
			print('ok, lets continue')

def symbvols():
	symb = '+', '-', '*', '/'
	s = input('Enter symbvol: ')
	if s in symb:
		return s

calculator()
n = symbvols()

if n == '+':
	print(num1 + num2)
else:
	print('try again')


