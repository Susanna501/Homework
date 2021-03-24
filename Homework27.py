'''6. NEw list
Write a python function which get a new list from a given list, consisting of the first repeating elements.
my_list = [“a”,”b”,”a”,”c”,”b”]
output “a”,”b”,”c”'''

def repeat():
	
	my_list = ["a","b","a","c","b"]
	new_list = []

	for i in my_list:
		if i not in new_list:
			new_list.append(i)

	return new_list

print(repeat())



'''7. How much  -You have word.txt file and in them you have one story.
Write a Python function that accepts this story and calculate the number of uppercase letters and lowercase letters.
Another Pause and MOre eyinG and SIDing AROUND eAch oTHer'''

def calculate():

	word_file = 'about_word.txt'

	try:
		with open(word_file) as f:
			word = json.load(f)
			print(word)

	except FileNotFoundError:
		
		var = input('Please enter your sentence: ')
		with open(word_file,'w') as f:
			word =json.dump(var,f)
			print('Hello',var)

	count_upper = 0
	count_lower = 0

	for i in word:
		if i.isupper():
			count_upper += 1

		elif i.islower():
			count_lower += 1

	return f"Uppercase is {count_upper} and Lowercase is {count_lower} "

print(calculate())


