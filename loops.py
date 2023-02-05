# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).



# While loops execute a set of statements as long as a condition is true.

people_mee=['john','paul','efe','mami'] 

#for person in people:
 #print(f"Current Person:{person}") 
 
for person in people_mee:
    if person == 'mami':
        break
print(f"Current Person: {person}")    

for person in people_mee:
    if person == 'mami':
        continue
print(f"Current Person: {person}")    
       
#for i in range(len(people)):
 #print(people[i])
         
         
#for i in range(0,11):
 #   print(f'Number: {i}')


#while
count =0
while count <= 10:
    print(f'Count: {count}')
    count += 1
    
    count =0
while count < 10:
    print(f'Count: {count}')
    count += 1 