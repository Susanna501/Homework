# name = 'Susanna'
# age = 33
# fname = 'Martirosyan'
# city = "Yerevan"


# info = {
# 	'Susik': [33,'Yerevan','Martirosyan'],
# 	'Arno' : [30,'NewYork','Gevorgyan']
# 	}

# def information():
# 	return 'Susanna jan'



# def add(x,y):
# 	return x + y
# 	


# def divide(x,y):
# 	try:
# 		return x / y
# 	except ZeroDivisionError:
# 		return "Don't divide by zero"



# def factorial(x):

# 	if x == 0:
# 		count = 1
# 	elif x < 0:
# 		count ='error'
# 	else:
# 		count = 1
# 		for i in range(2, x +1):
# 			count *= i
# 	return count


# def gcd(x,y):

# 	if x == 0 or y == 0:
# 		count ='error'
# 	else:
# 		count = 1
# 		if x > y:
# 			start = y
# 		else:
# 			start = x
# 		for i in  range(start, 0, -1):
# 			if x % i == 0 and y % i ==0:
# 				return i
# 	return count


# def fibonacci(n):
	# x,y = 0, 1
	# c = []
	# while y < n:
	# 	c.append(str(y))
	# 	x, y = y, x + y
	# return ' '.join(c)


# def result():
# 	# return 'Hi Susanna jan' 
# 			'''Or '''
# 	print('Hi Susanna jan')
	

# person  = {
# 		'name': 'Sona',
# 		'age': 33,
# 		'country': 'Yerevan'
# 		}





'''Homework28'''
def factorial2(x):

	if x == 0:
		count = 1
	elif x < 0:
		count ='error'
	else:
		count = 1
		end = x + 1
		for i in range(2, end):
			count *= i
	return count
	


# V=πr^2h and A=2πrh+2πr^2

def cylinder_volume_and_area(x,y):
	pi = 3.14
	r = int(input('please enter r: '))
	h = int(input('please enter h: '))

	vol = pi *r *r * h
	area = 2 * pi *r * h + 2 * pi * r * r
	return f"volume is {vol} and area is {area}" 



# V = 4/3*π*r3 and A = 4*π*r2

def sphere_volume_and_area(x):
	pi = 3.14
	r = float(input('please enter r: '))

	vol = 4 / 3 * pi * r **3
	area = 4 * pi * r **2
	return f"volume is {vol} and area is {area}" 



# one radian = pi/180: 90 radian = 1.57

def degree_to_radian(a):
	pi = 3.14
	one_radian = pi/180
	radian = 90 * pi / 180
	return radian

'''OR'''
	# r = float(input('enter your radian number: '))
	# radian = r * pi / 180
	


# numbers(9) Output: (2, 3, 5, 7)


def allprimes(a):
	x = 2
	end = a + 1
	c = []
	for i in range(x,end):
		for j in range(2,i):
			if i % j == 0:
				break
		else:
			c.append(i)
	
	return f"Output is {c}"












