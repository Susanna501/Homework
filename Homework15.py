'''5. Sign in
Create python program where you want to check if input word is palindrome or no.
if yes print Open otherwise Trash Sample Input: RACECAR Sample Output: Open'''

# palin = input('write your palindrome: ')

# if palin == palin[::-1]:
# 	print('OPen')
# else:
# 	print('TRash')


'''6. Sign in Create python program to convert string to a list.'''
# string = input('your input: ').split(" ")
# print(string)


'''7. Even Numbers
Create python program which will show all even numbers in your string. Note: you have input where 
have 5 numbers: Sample Input: 12 21 15 19 8   Sample Output: 12 8'''

# number = [12,21,15,19,8]
# for i in number:
# 	if int(i) % 2 == 0:
# 		print(i,'your number is even')
# 	else:
# 		print(i,'your number is odd')



'''8. Odd
Write a Python program to select the odd items of a list. And delete even items.'''

# number = [12,21,15,19,8,14,100,3]
# for i in number:
# 	if int(i) % 2 == 1:
# 		print('odd',i)
# 	else:
# 		del i
		


'''9. Santa
Your group have 5 people and each of them can take one name and when take this name is delete
from this list.And he can not take his name:'''

import random as r

names = ['Ani','Susik','Gevor','Anjela']
names2 = ['Ani','Susik','Gevor','Anjela']
group1=''

count = 0
for i in names:
	group = r.choice(names2)
	c = names2.index(group)
	del names2[c]
	count += 1
	group1 += str(count) + " " +group + ' ' + i + ' ' + ' \n' 


print(group1)

'''10. Duplicate
Create a python program which delete allduplicate items in list.'''
# num = [3, 'susik', 14.6, 16, -2, 'susik', 43, 16]

# c = []
# for i in num:
# 	if i not in c:
# 		c.append(i)
# print(c)	