'''Task1-Write a python program to check have your name ‘a’ or no.You have 2 input.'''
name1 =input('name1: ') 
name2 =input('name2: ')
res_name1 = 'a' in name1 
res_name2 = 'a' not in name2 
print('my name is true: ',res_name1)
print('my name is false: ',res_name2)


'''Task2-Write a python program to check if there are bananas, 
oranges and apples in your fridge։'''
banana = input('banana: ')
oranges = input('oranges: ')
apples = input('apples: ')
fridge = input('fridge։ ')

res_banana = banana == 'y' or banana =='yes'
print('banana:',res_banana)

res_oranges = oranges == 'y' or oranges =='yes'
print('oranges:',res_oranges)

res_apples = apples == 'y' or apples =='yes'
print('apples:',res_apples)

res_fridge = fridge == 'y' or fridge =='yes'
print('fridge:',res_fridge)

ka_banan = res_banana and res_fridge
print('Banan ka: ',ka_banan)

ka_orange = res_oranges and res_fridge
print('oranges ka: ',ka_orange)

ka_apple = res_apples and res_fridge
print('apple ka: ',ka_apple)

'''Task3- Given a number x. Check following conditions: x is less or equal to -8 or x is greater than 12
x is greater than 10 and is less or equal to 50 x is greater than -10 and is less than 10
x isn’t equal to 20 or x is greater than 50 Print the results (they should be True or False)'''

x = 5
res1 = x <= 8 or x > 12
print(res1)
res2 = x > 10 and x <= 50
print(res2)
res3 = x > -10 and x < 10
print(res3)
res4 = x != 20 or x > 50
print(res4)

'''Task4- Write a python program to check if there are bananas, oranges and apples in your
fridge, and if you don’t have one of them you should go buy this , and check have you at
home light if not, take those items out of the fridge։'''
banana = input('banana: ')
oranges = input('oranges: ')
apples = input('apples: ')
light = input('light: ')

res_banana = banana == 'y' or banana =='yes'
print('banana:',res_banana)

res_oranges = oranges == 'y' or oranges =='yes'
print('oranges:',res_oranges)

res_apples = apples == 'y' or apples =='yes'
print('apples:',res_apples)

res_light = light == 'y' or light =='yes'
print('fridge:',res_light)

cka_banan = not res_banana
print('buy banana: ',cka_banan)

cka_orange = not res_oranges
print('buy oranges : ',cka_orange)

cka_apple = not res_apples
print('buy apple: ',cka_apple)

ka_banan = res_banana and not res_light
print('out of banana: ',ka_banan)

ka_orange = res_oranges and not res_light
print('out of oranges : ',ka_orange)

ka_apple = res_apples and not res_light
print('out of apple: ',ka_apple)



banana = input('banana: ')
oranges = input('oranges: ')
apples = input('apples: ')
light = input('light: ')

res_ban = banana == 'y' or banana == 'yes'
print('banana:',res_ban)
res_org = oranges == 'y' or oranges == 'yes'
print('banana:',res_org)
res_app = apples == 'y' or apples == 'yes'
print('banana:',res_app)
res_lgt = light == 'y' or light == 'yes'
print('banana:',res_lgt)
ban_cka = not banana 
print('gni',ban_cka)
org_cka = not oranges
print('gni',org_cka)
app_cka = not apples
print('gni',app_cka)
ka_b = res_ban and not res_lgt
print('hani banana: ',ka_b)
ka_o = res_org and not res_lgt
print('hani banana: ',ka_o)
ka_a = res_app and not res_lgt
print('hani banana: ',ka_a)