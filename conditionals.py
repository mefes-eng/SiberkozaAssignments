# If/ Else conditions are used to decide to do something based on something being true or false
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# Logical operators (and, or, not) - Used to combine conditional statements
# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

 #comparisions
   
   #basic if
if x_mee>y_mee:
 print(f'{x_mee} is greater than{y_mee}')
 
 if x>y:
  print(f'{x_mee} is greater than{y_mee}')
else:
 print(f'{y_mee} is greater than{x_mee}')
 
 #elif
if x>y:
  print(f'{x_mee} is greater than{y_mee}')
elif  x==y:
      print(f'{x_mee} is equal to {y_mee}')
else:
 print(f'{y_mee} is greater than{x_mee}') 
 
 #nested if
if x_mee>2:
     if x_mee <= 10:
         print(f'{x_mee} is greater than 2 and less than or equal to 10')
if x_mee>2 and x_mee<=10:
    print(f'{x_mee} is greater than 2 and less than or equal to 10')
     
if x_mee>2 or x_mee<=10:
    print(f'{x_mee} is greater than 2 or less than or equal to 10')
    
    #not
if not(x_mee==y_mee):
    print(f'{x_mee} is not equal to {y_mee}')
 
numbers_mee=[1,2,3,4,5]
if x_mee in numbers_mee:
 print(x_mee in numbers_mee)
 
 if x not in numbers_mee:
     print(x_mee in not numbers_mee) #??? not ??
     
     
     #is
if x_mee is y_mee:
         print(x_mee is y_mee)

