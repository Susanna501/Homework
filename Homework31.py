
'''1.Odd Write a recursive function to determine whether all digits of the number are odd or not.
Input Output
4211133 False
7791 True
5 True'''

number = int(input('My number: '))

def all_digits(number):

	if number % 2 == 0:
		return True
	elif number % 2 != 0:
		return False
	else:
		return odd(number)

if all_digits(number):
	print(number, 'number is even')
else:
	print(number, 'number is odd')




'''2. Threading 
Write a python function all even number in 10.000 use threading and print time.'''

import threading
import time

even_number = int(input('My number: '))
c = []
def all_even(start,even_number):

	for i in range(start,even_number + 1):
		if i % 2 == 0:
			c.append(i)
			# print(c)
			time.sleep(0.01)

start = time.time()
t1 = threading.Thread(target = all_even, args =(1,10))
t2 = threading.Thread(target = all_even, args =(11,20))
t3 = threading.Thread(target = all_even, args =(21,30))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(time.time()-start)




'''3. Numbers
Given N number. Write a recursive function that should print from 1 to N numbers.
Input Output 5    1, 2, 3, 4, 5'''

num = int(input('My number: '))

def n_number(num):
	if num == 1:
		print(num)
	else:
		n_number(num - 1)
		print(num)

n_number(num)



'''4. Longest Word
Write a python program to find the longest word from the file content.Need to use
<try-except> block in the file reading process and print time. example:
1. try:
2. with open("filename.txt") as file:
3. some code
4. except:
5. do something
6. Function call: find_long_word("filename.txt")
7. Function output: "LongestWord"'''

import time
file_name = 'LongestWord.txt'

def longest_word(file_name):

	try:
		with open(file_name) as f:
			maxi = 0
			for i in file_name:
				if len(i) > maxi:
					maxi = len(i)
					time.sleep(0.1)
	
	except FileNotFoundError:
		print('sorry, there are not found your file: ')
	
	finally:
		print('the longest word is',i)
	
start = time.time()
longest_word(file_name)
print(time.time()-start)

