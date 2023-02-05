# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 


# A Set is a collection which is unordered and unindexed. No duplicate members.


fruits_mee=("apples","oranges","grapes")
#fruits2=tuple(("apples","oranges","grapes"))

fruits2_mee=("apples",)

#get value
print(fruits_mee[1])

del fruits2_mee

print(len(fruits_mee))
'''
#create a set 
'''
fruits_set_mee={"apples","oranges","mango"}

#check if in set
print("apples" in fruits_set_mee)

#add to set
fruits_set_mee.add("grape")
fruits_set_mee.add("apples")


#remove from set
#fruits_set.remove("grape")

#clear set
#fruits_set.clear()

#delete set
#del fruits_set

print(fruits_set_mee) 