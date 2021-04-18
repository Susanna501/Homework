'''1. Calculator- class'''
# class Calculator:
# 	"""All about calculator and their properties"""
# 	def number(self):
# 		while True:
# 			try:
# 				x = int(input('Enter your number: '))
# 				return x
# 			except ValueError:
# 				print("Sorry,input only numbers ")

# 	def choice(self):
# 		sym = '+','-','/','*'
# 		symb_input = input('please input your symbvol: ')
# 		if symb_input in sym:
# 			return symb_input

# 	def result(self):
# 		x = self.number()
# 		c = self.choice()
# 		y = self.number()
# 		print(x,y)

# 		if c == '+':
# 			print(x + y)
# 		elif c == '-':
# 			print(x -y)
# 		elif c == '*':
# 			print(x * y)
# 		else:
# 			print(x/y)

# t1 = Calculator()
# print(t1.result())



'''2. Car -Create a class for Car and Person'''

# class Car:
# 	"""Everything about car and their property"""
# 	def __init__(self, model, color, year, power):
# 		self.model = model
# 		self.color = color
# 		self.year = year
# 		self.power = power

# 	def cars(abc):
# 		return f"My new car is {abc.model}, it is {abc.color} and created in {abc.year} and the max power is {abc.power} km"

# d = Car('BMW','White',2021,320)
# print(d.cars())




# class Person:
# 	'''Information about person '''
# 	def __init__(self, fname, lname, age, eye_color, gender, education):
# 		self.fname = fname
# 		self.lname = lname
# 		self.age = age
# 		self.eye_color = eye_color
# 		self.gender = gender
# 		self.education = education
# 		self.email = fname + '.'+ lname +'@gmail.com'

# 	def myfunction(self):
# 		# a = self.fname
# 		return f"My name is {self.fname} {self.lname} I am {self.age} my eye color is {self.eye_color}\
# 		 i am {self.gender}I hava a {self.education} degree and my email is {self.email}"

# t1 = Person('Susanna', 'Martirosyan',33,'brown','female', 'Master')
# print(t1.myfunction())





'''Change. Create a class Change:You have 3 methods in your class:
Usd --- Eur
Usd --- Amd
Usd --- Ru'''

# class Change():
# 	'''more details about change and currency'''
# 	def __init__(self, amount):
# 		self.amount = amount

# 	def USD_AMD(self):
# 		return f"{self.amount}$ is {self.amount * 520}AMD"

# 	def AMD_USD(self):
# 		return f"{self.amount}AMD is {self.amount * 0.0019}$"

# 	def USD_EUR(self):
# 		return f"{self.amount}$ is {self.amount * 0.82}EU"		

# 	def EUR_USD(self):
# 		return f"{self.amount}EU is {self.amount * 1.17}$"

# 	def USD_RU(self):
# 		return f"{self.amount}$ is {self.amount *73}RU"		

# 	def RU_USD(self):
# 		return f"{self.amount}RU is {self.amount * 0.013}$"

# amount  = int(input('input your amount: '))
# currency_from = input('From: ')
# currency_to = input('To: ')
# t = Change(amount)

# if currency_from == "AMD" and currency_to == "USD":
# 	print(t.AMD_USD())
# elif currency_from == "USD" and currency_to == "AMD":
# 	print(t.USD_AMD())
# elif currency_from == "USD" and currency_to == "EUR":
# 	print(t.USD_EUR())
# elif currency_from == "EUR" and currency_to == "USD":
# 	print(t.EUR_USD())
# elif currency_from == "USD" and currency_to == "RU":
# 	print(t.USD_RU())
# else:
# 	print(t.RU_USD())

