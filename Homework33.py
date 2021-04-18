"""1- Max 
Write a python class to find max, min num and and sum in your list: don’t use max sum and min function"""

# class Maximum:
# 	"""everything about max class and function"""
# 	num =[5,-303,14,804,105,-4,16]
# 	def __init__(self, num):
# 		self.num = num
	
# 	def maxi(self):

# 		max_namber = 0
# 		min_namber = 0

# 		for i in self.num:
# 			if i > max_namber:
# 				max_namber = i
# 			elif i < min_namber:
# 				min_namber = i 

		
# 		return f"Max number = {max_namber}, Min number = {min_namber}, SUM number = {max_namber + min_namber}"

# m = Maximum([5,-303,14,804,105,-4,16])
# print(m.maxi())





"""Highest 2 
Write a python class to find two highest values in your dict:"""

# class Highest:
# 	'''All About Highest class and theri properties'''
# 	my_dict = {'D': 53, 'E': 102, 'F': 61, 'C': 35, 'B': 26, 'A': 97}

# 	def __init__(self, my_dict):
# 		self.my_dict = my_dict


# 	def add_dict(self):
# 		new_value = sorted(self.my_dict.values())
# 		res_value = new_value[::-1]
# 		final_result = res_value[:2]

# 		for i in final_result:
# 			for j in self.my_dict:
# 				if self.my_dict[j] == i:

# 					return f"The highest 2 values are: {j} {i}"

# h = Highest({'D': 53, 'E': 102, 'F': 61, 'C': 35, 'B': 26, 'A': 97})
# print(h.add_dict())




''' 3 -Inheritance
Write a python class where your child class takes all methods in parent class and print them.'''

# class Employee:
# 	'''All about employee'''
# 	def __init__(self, firstname, lastname, pay):
# 		self.fname = firstname
# 		self.lname = lastname
# 		self.pay = pay

# 	def fullname(self):
# 		return f"{self.fname} {self.lname}"

# 	def salary_raise(self):
# 		self.pay = self.pay * 1.15

# class Supplier(Employee):
# 	'''All about Supplier which is child in parent class '''
# 	def __init__(self, firstname, lastname, pay, prog_lang):
# 		super().__init__(firstname, lastname, pay)
# 		self.prog_lang = prog_lang

# # emp_1 = Employee('Susik','Martirosyan',500000)
# # emp_2 = Employee('Ani','Melkonyan', 600000)

# emp_1 = Supplier('Susik','Martirosyan',500000, 'Python')
# emp_2 = Supplier('Ani','Melkonyan', 600000, "C++")

# print(emp_1.fullname())
# print('emp_1 programming languages is',emp_1.prog_lang)

# print(emp_2.fullname())
# print('emp_2 programming languages is',emp_2.prog_lang)

# # print('Before raised salary is',emp_1.pay)
# # emp_1.salary_raise()
# # print('After raised salary is',emp_1.pay)
# # print(emp_2.pay)






'''4 Rectangle 
Write a Python class named Rectangle constructed by a length and width and a method
which will compute the area of a rectangle.A = w*l'''

# class Rectangle:
# 	'''All about rectangle'''
# 	def __init__(self, width, length):
# 		self.w = width
# 		self.l = length

# 	def area_of_rectangle(self):
# 		return self.w  * self.l

# r = Rectangle(5,13)
# print('The area of rectangle is',r.area_of_rectangle())





'''5- Polymorphism 
Write a python class where we use polymorphism: Example:
a.country() - Erevan
b.country() - Paris'''

# class Armenia:
# 	"""All about Armenia"""
# 	def country(self):
# 		print('Yerevan is the capital of Armenia')

# class France:
# 	"""All about France"""
# 	def country(self):
# 		print('Paris is the capital of France')

# a = Armenia()
# b = France()

# a.country()
# b.country()