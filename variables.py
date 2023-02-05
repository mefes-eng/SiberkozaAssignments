# A variable is a container for a value, which can be of various types


'''This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes'''



'''VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one'''


# x= 9  #integer
# y= 3.4  #float
# name= 'efe'   #string
# dr_ingame= True  #boolean

#Multiple assignment

x_mee,y_mee,name_mee,dr_ingame_mee =(9,3.4,'efe',True)

a=x_mee+y_mee

print(x_mee,y_mee,name_mee,dr_ingame_mee,a)

x_mee=str(x_mee)
y_mee=int(y_mee)
z=float(y_mee)

print(type(x_mee))
print(type(y_mee),y_mee,z) 