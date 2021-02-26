'''Task1. Write a Python program to count the elements in a list 
until an element is a tuple.'''

tuplelist = [1,2,3,4,(5,6),7,8]
a = 0
for i in tuplelist:
	if isinstance(i, tuple):
		break
	a += 1
print('My tuple is: ',a)



'''Task2. Write a Python program to reverse a tuple.'''
mytup = (10,20,30,40,'susik')
myreverse = reversed(mytup)
print(tuple(myreverse))

'''or'''
mytup = (10,20,30,40,'susik')
print(mytup[::-1])



'''Task3. Write a Python program to find the length of a tuple.'''
mylist = ('NewYork','London',61,'Amsterdam','Madrid',25,3)
c = 0
for i in mylist:
	c += 1
print('My tuple length is: ',c)

'''or'''
mylist = ('New York','London',61,'Amsterdam','Madrid',25,3)
print(len(mylist))



'''Task4. Write a Python program to convert a tuple to a string.'''
tup = ('S','u','s','a','n','n','a',' ','M','a','r','t','r','o','s','y','a','n')
myname = ''.join(tup)
print(myname)



'''Task5. Write a Python program which calculate the count of item in
tuple for example: my_tuple = (1,12,15) output:28.'''
my_tuple = (1,12,15)
x = sum(my_tuple)
print(x)

'''or'''
my_tuple = (1,12,15)
count = 0
for i in my_tuple:
	count += i
	
print('My tuple is: ',count)



'''Task6. Write a Python program to find name in tuple.'''
name = ('Ani','Susik','Lilit','Ani','Vika','Mary')
user = input('your name is: ')

if user in name:
	print('yes, you are right')
else:
	print('sorry, please try again')




