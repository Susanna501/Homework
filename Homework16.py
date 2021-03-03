'''Task1.Write a Python program to sort a dictionary by value.'''

mydict = {1: 13, 4: -1, 11: 2, 6: 7, 2: 25, 9: -17}
# print(mydict)

res = sorted(mydict.values())
# print(res)
count = 0

for i in res:
	count += 1
	for e in mydict:
		if mydict[e] == i:
			print(count,e,i)



'''Task2. Write a Python program to add a key to a dictionary.'''

my_dict = {'name': 'Zara','Age': 33,'city': 'Armenia'}
my_dict['email'] = 'susik@mail.ru'  # 1st version
my_dict.update({'year': 2021})      # 2nd version
print(my_dict)


'''Task3. Write a Python program to check whether a given key already exists in a dictionary.'''

my_dict = {'name': 'Zara','Age': 33,'city': 'Armenia'}
my_key = input('enter your key: ')

if my_key in my_dict.keys():
	print('There are: The Key value is: ', my_dict[my_key])
else:
	print('Please try again')



'''Task4. Write a Python program to merge two Python dictionaries.
dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
output: {'a': 50, 'b': 700, 'c': 400, 'd': 600}'''

dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
res = dict1.copy()
res.update(dict2)
print(res)

'''version2'''

for i in dict2:
	dict1[i]= dict2[i]    
print(dict1)


'''Task5. Write a Python program to multiply all the values in a dictionary. For example:
mydict = {'a':1,'b':2,'c':12} output: 24'''

mydict = {'a':1,'b':2,'c':12}
my_value = 1

for i in mydict.values():
	my_value *= i
print('My value is: ', my_value)



'''Task6. Create a Python program to find the highest 3 values in a dictionary.
{'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67} output: {'F': 69, 'A': 67, 'D': 56}'''

dict1 = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
val = sorted(dict1.values())
value_res = val[::-1]
fin_res = value_res[:3]

for i in fin_res:
	for j in dict1: 
		if dict1[j] == i:
			print('The highest 3 values: ', j,i)





'''other version '''
# dict1 = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# val = sorted(dict1.values())
# value_res = val[::-1]
# fin_res = value_res[:3]

# res= []
# for i in dict1:
# 	if dict1[i] in fin_res:
# 		res.append(i)
# print('highest val:', res,fin_res)





