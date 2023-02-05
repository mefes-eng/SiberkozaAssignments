# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


# String Formatting

# String Methods

name_mee="Efe"
age_mee=21

#concanate
print('Hello my name is ' + name_mee + ' and I am ' + str(age_mee))

#argument by position
print(' My name is {name_mee}   and I am   {age_mee}'.format(name_mee=name, age_mee=age) )

#F-string
print(f"Hello my name is {name_mee} and I am {age_mee}")

#string types


s="hello worllld"

print(s.capitalize())
print(s.upper())
print(len(s))