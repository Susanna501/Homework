'''5. find index
Given a list of numbers and a number. Find the index of a first element which is equal to that 
number. If there is not such a number, that find the index of the first element which is the 
closest to it. Input Output
[21, -9, 15, 2116, -71, 33], -71 4
[ 36, -12, 47, -58, 148, -55, -19, 10], -56 5'''


def find_index(old_list, search, start,stop):
	for i in range(0,stop):
		if old_list[i] == search:
			return i
	# return -1
	
	if start > stop:
		return False
	else:
		mid = (start + stop)//2
		if search == old_list[mid]:
			return mid
		elif search < old_list[mid]:
			return find_index(old_list,search,start, mid -1)
		else:
			return find_index(old_list,search, mid +1, stop)

search = -71
start = 0	
old_list =[21, -9, 15, 2116, -71, 33]
stop = len(old_list)
res = find_index(old_list, search, start,stop)

if search == False:
	print('Item', search,'not found')
else:
	print('item',search,'found at index: ', res)



'''ooor'''

def find_index(old_list,length, my_number):

	for i in range(0,length):
		if old_list[i] == my_number:
			return i
		# else:
		# 	old_list[i] == my_number:
	return -1
		
old_list =[21, -9, 15, 2116, -71, 33]
my_number = -71
length = len(old_list)
res = find_index(old_list, length, my_number)

if res == -1:
	print('the element is not found here')
else:
	print('the element is found', my_number, res)




'''6. New Dict
Define a function which can generate a dictionary where the keys are numbers between 1 and N (both included) and
the values are square of keys. The function should print the dict.Example :
N = 5
{1: 1, 2:4, 3:9, 4:16, 5:25}'''

def new_dict(n):

	d = {}
	for i in range(1,n +1):
		d[i]= i **2
	return d

print(new_dict(5))



'''7. INVERT Dict
Given an dict. Invert it (keys become values and values become keys).If there is more than key for that given value create an list.
Input{ a: ‘1’, b: ‘2’, c: ‘2’ }
Output { 1: ‘a’, 2: [‘b’, ‘c’] }'''


old_dic = {'a': 1,'b': 2, 'c':2}  

def invert_dict(old_dic):
	new_dict = {}

	for i,j in old_dic.items():
		if not j in new_dict.keys():
			new_dict[j]= []
		new_dict[j].append(i)
	return new_dict

	# output i jamanak valunery sax list en tpum, nayem vor menak duplicatnery tpi list
print(invert_dict(old_dic))



'''8. FIBONACCI Write a function using recursion to find fibonacci numbers:'''

def fibonaci(x):
	if x ==0 or x ==1:
		return 1
	else:
		return fibonaci(x-1)+ fibonaci(x-2)
print(fibonaci(10))






