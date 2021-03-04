'''1.Calculator'''

# def digits():
# 	global x,y
# 	x = input('enter your number: ')
# 	y = input('enter your number: ')
	
# 	if x.isdigit() and y.isdigit():
# 		x,y = int(x),int(y)
# 		return 'ok'

# def symbvol():
# 	symb = '+','-','/','*'  # tuple
# 	a = input('input your symbvol: ')
# 	if a in symb:
# 		return a

# digits()
# k = symbvol()

# if k == '*':
# 	print(x * y)



'''2.Write a python program to find max of two numbers.'''
# def maximum(x,y):
# 	if x > y:
# 		return x
# 	return y

# print(maximum(7,2))



'''3.Write a python program to sum all numbers.'''
# def sum_total(num):
# 	amount = 0
# 	for i in num:
# 		amount += i
# 	return amount

# print(sum_total((6,2,7)))


'''4.Write a python program to multiply all numbers.'''
# def multy_total(num):
# 	amount = 1
# 	for i in num:
# 		amount *= i
# 	return amount

# print(multy_total((6,2,7)))



'''5.Write a python program to sum all letter and number in your string.'''
# def summa(number):
# 	count1 = 0
# 	count2 = 0
# 	number = input('enter: ')

# 	for i in number:
# 		if i.isdigit():
# 			count1 += 1
# 		else:
# 			count2 += 1
			
# 	return f"numbers {count1} and letters {count2} "

# print(summa(""))


'''6.You are given a program that takes all 3 passengers ages as inputs and inserts them in
a list. Complete the program so that If it finds a value less than 16, it breaks the
loop and outputs "Too young! ". If the age requirement is satisfied, the program outputs "Get ready!".'''

# def passengers(num):

# 	for i in num:
# 		if i >= 16:
# 			return ('Get ready')
	
# 	else:
# 		return('Too young')
# 		break

# pas1 = int(input('1st passangers: '))
# pas2 = int(input('2nd passangers: '))
# pas3 = int(input('3rd passangers: '))
# num = [pas1, pas2, pas3]

# passengers(num)



# def passengers():
# 	global pas1,pas2,pas3

# 	pas1 = int(input('1st passangers: '))
# 	pas2 = int(input('2nd passangers: '))
# 	pas3 = int(input('3rd passangers: '))

# 	while True:
# 		if pas1 <= 16 and pas2 <= 16 and pas3 <= 16:
# 			return('Too young')
# 			break

# 		else:
# 			return('Get ready')
# passengers()








