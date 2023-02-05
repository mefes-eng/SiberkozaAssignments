# A List is a collection which is ordered and changeable. Allows duplicate members.

#create list
numbers_mee=[1,2,3,4,5]
fruits_mee=["apples","oranges","grapes","pears"]


#use a constructor
numbers2=list((1,2,3,4,5))

#get a value
print(fruits_mee[1])

#get length
print(len(fruits_mee))

#append to list
fruits_mee.append("mangos")

#remove from list
fruits_mee.remove("grapes")

#insert into position
fruits_mee.insert(2,'strawberries')

#change value
fruits_mee[0]="blueberries"

#remove with pop
fruits_mee.pop(2)

#reverse list
fruits_mee.reverse()

#sort list
fruits_mee.sort()

#reverse sort
#fruits.sort(reverse=True)

print(fruits_mee) 
