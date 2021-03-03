'''Write a python program which have 5 input (questions).
You should check if the answers is right print True otherwise False'''

question1 = input('What is your name? Susanna: ')
question2 = input('Where are you from? Armenia: ')
question3 = int(input('How old are you? 15: '))
question4 = input('Where do you study? Arnoyi mot: ') 
question5 = input('Where do you work? At home: ')

result1 = question1 == 'y' or question1 == 'yes'
result2 = question2 == 'y' or question2 == 'yes'
result3 = question3 == 15
result4 = question4 == 'y' or question4 == 'yes'
result5 = question5 == 'y' or question5 == 'yes'
print('Res1: ',result1,'\nRes2: ',result2,'\nRes3: ',result3,'\nRes4: ',result4,'\nRes5: ',result5)



'''Write a python program which have a lot of input (employee data for example 
min_year =17,max_year = 25). And if he meets your requirements, he will be hired.'''

# age = int(input('employee age: '))
# experience = int(input('employee experience: '))
# sex = input('employee male-female: ')== 'male'

# min_age = 17
# max_age = 25
# experience_emp = 7 # and more
# result_age = age >= min_age and age <= max_age
# result_exp = experience >= experience_emp
# result_sex = sex
# print('res_age: ',result_age, '\nres_exp: ',result_exp, '\nres_sex: ',result_sex)



'''Write a python program which consider (a+b)^3 (5 + 6)^3 = ?
(a+b)^3=a^3 +3*a^2*b+3*a*b^2+b^3
(a+b)^3=(a+b)(a+b)(a+b)=(a^2+2ab+b^2)(a+b)=a^3 +3*a^2*b+3*a*b^2+b^3
(5 + 6)^ 3 = 5 **3 + 3* 5**2 *6 + 3*5* 6**2 + 6**3 '''

# import math
# a = 5
# b = 6
# res = 5**3 + 3*5**2*6 + 3*5*6**2 + 6**3
# print(math.sqrt(res))
 


'''Task1-The competition rules- there are 3 families and 1 box with a lot of balls,
if the input result equal to ball number this family win in competition '''

# import random
# box_number = random.randint(1,10)
# family_mamber_1 = int(input('family1: '))
# family_mamber_2 = int(input('family2: '))
# family_mamber_3 = int(input('family3: '))

# res_fam1 = family_mamber_1 >= box_number  
# res_fam2 = family_mamber_2 >= box_number 
# res_fam3 = family_mamber_3 >= box_number 

# print('Random1: ',box_number,'Next level: ',res_fam1, 
# 	'\nRandom2: ',box_number,'Next level: ',res_fam2,
# 	'\nRandom3: ',box_number,'Next level: ',res_fam3,)



''' your monthly salary is 1547usd, you should pay.
utility cost, car rent, home rent, insurance it the remainder is even or odd '''

# salary = 1547
# utility_cost = int(input('Utility: '))
# car_rent = int(input('Car_rent: '))
# home_rent = int(input('Home_rent: '))
# insurance = int(input('Insurance: '))

# result = (salary - utility_cost - car_rent - home_rent - insurance)
# total_even = result % 2 == 0
# total_odd = result % 2 == 1

# print('Total remainder: ',result, 'Even: ',total_even)
# print('Total remainder: ',result, 'Odd: ',total_odd)


