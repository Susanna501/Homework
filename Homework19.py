'''1. Write a Python program to create a set.'''
set1 = {1,3,'a', True,-3}
print(set1)

x = set(['aaa',False,-33, 142])
print(x)


'''2. Write a Python program to iteration over sets.'''
set1 = {1,3,'a',-3,'b',143}
for i in set1:
	print(i)


'''3. Write a Python program to add member(s) in a set.'''
sets = {'apple','banana','kiwi','melon'}
sets.add('orange')
print(sets)

sets = {'apple','banana','kiwi','melon'}
new_set = {'orange','cherry','papaya','banana'}
sets.update(new_set)
print(sets)


'''4. Write a Python program to remove item(s) from set'''
set_2 = {'orange','cherry','papaya','banana'}
set_2.remove('papaya')
print(set_2)

set_2 = {'orange','cherry','papaya','banana'}
set_2.pop()
print(set_2)


'''5. Write a Python program to remove an item from a set if it is present in the set.'''
set_2 = {'orange','cherry','papaya','banana'}
set_2.discard('cherry')
print(set_2)


'''6. Write a Python program to create an intersection of sets.'''
set1 = {'apple','banana','kiwi','cherry'}
set2 = {'google','microsoft','apple'}
set3 = set1.intersection(set2)
print(set3)


'''7. Write a Python program to create a union of sets.'''
set1 = {'apple','banana','kiwi','cherry'}
set2 = {'google','microsoft',1,3,14,'kiwi'}
set3 = set1.union(set2)
print(set3)


'''8. Write a Python program to issubset and issuperset.'''
set1 = {'apple','banana','kiwi'}
set2 = {1,'kiwi',22,143,'banana','orange','apple',-36,'lemon'}
set3 = set1.issubset(set2)
print(set3)

# set1 = {1,'kiwi',22,143,'banana','orange','apple',-36,'lemon'}
set2 = {'apple','banana','kiwi'}
set3 = set1.issuperset(set2)
print(set3)


'''9. Write a Python program to clear a set.'''
set1 = {1,'kiwi',22,143,'banana','orange','apple',-36,'lemon'}
set1.clear()
print(set1)


'''10. Write a Python program to find maximum and the minimum value in a set.'''
x = {1,15,362,74,-6,25,-78,-105}
print(max(x))
print(min(x))


'''11. Write a Python program to find the length of a set'''
set1 = {1,'kiwi',22,143,'banana','orange','apple',-36,'lemon'}
print(len(set1))


