# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create dict
person_mee= {
    'first_name': 'efe',
    'last_name':'elmas',
    'age':30
}
#use a constructor
#person2=dict('first_name='efe',last_name='elmas')

#get value
print(person_mee['first_name'])
print(person_mee.get('last_name'))


person_mee['phone']='0507-057-1656'

#get dict keys
print(person_mee.keys())

#copy dict
person2=person_mee.copy()
person2['city']='Boston'

print(person2)


#remove item
del(person_mee['age'])
person_mee.pop('phone')

#clear
person_mee.clear()

#get length
print(len(person2))

print(person_mee)

#list of dict
people=[
{'name':'Efe','age':21},
{'name':'Yigit','age':17},

]

print(people[1]['name'])