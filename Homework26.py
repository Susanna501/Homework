'''1. Write a Python program to add info in JSON file about you.'''
import json

# bio = 'about_susik.json'

# member1 = {'name': 'Susik',
# 		 'age': 30,
# 		 'city':'Yerevan',
# 		 'salary': 120,
# 		 'height': [1, 162, 170],
# 		 'eye_color': 'Brown'}

# member2 = {'name': 'Ani',
# 		 'age': 30,
# 		 'city':'New York',
# 		 'salary': 450000,
# 		 'height': 170,
# 		 'eye_color': 'Green'}

# allmembers = [member1,member2]
# with open(bio,'w') as f:
# 	json.dump(allmembers,f)

# bio_file = open(bio)
# json_file = json.load(bio_file)

# for i in json_file:
# 	if i['name'] == 'Susik':
# 		i['email'] = 'susik@mail.ru'
# 	if i['name'] == 'Ani':
# 		i['email'] = '--'

# for i in json_file:
# 	print('\nMember name is', i['name'])
# 	print('Member age is', i['age'])
# 	print('Member city is', i['city'])
# 	print('Member salary is', i['salary'])
# 	print('Member height is', i['height'])
# 	print('Member eye_color is', i['eye_color'])
# 	print('Member email is', i['email'])
	


'''2. Write a Python program to get info in JSON file about you.'''

# def test(file):

# 	with open(file,'w') as f:
# 		json.dump({'Name': 'Susik','city': 'Yerevan','Age': 33},f)

# 	with open(file) as f:
# 		c = json.load(f)
# 		print(c)

# 		return  c

# file = 'user.json'
# print(test(file))




'''3. Write a Python program to check if your json file have this info.'''

# info = 'info_susik.json'

# member1 = {'name': 'Susik',
# 		 'age': 30,
# 		 'city':'Yerevan',
# 		 'salary': 120,
# 		 'height': [1, 162, 170],
# 		 'eye_color': 'Brown'}

# allmembers = [member1]
# with open(info,'w') as f:
# 	json.dump(allmembers,f)

# info_file = open(info)
# json_file = json.load(info_file)
# your_input = input('enter your answer:')

# for i in json_file:
# 	# print(i.values())
# 	if your_input in i.values():
# 		i['eye_color'] = 'Green'
# 		for i in json_file:
# 			print('\nMember name is', i['name'])
# 			print('Member age is', i['age'])
# 			print('Member city is', i['city'])
# 			print('Member salary is', i['salary'])
# 			print('Member height is', i['height'])
# 			print('Member eye_color is', i['eye_color'])
# 	else:
# 		print('empty')









