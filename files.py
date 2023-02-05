# Python has functions for creating, reading, updating, and deleting files.

#open a file
myFile_mee =open('myfile.txt','w')

#get some info
print('name:',myFile_mee.name)
print('Is Closed: ',myFile_mee.closed)
print('Opening Mode: ',myFile_mee.mode)

#write to file
myFile_mee.write('I love Python')
myFile_mee.write('and Javascript')
myFile_mee.close()

#append to file
myFile_mee= open('myFile_mee.txt','a')
myFile_mee.write('I also like PHP')
myFile_mee.close()

#read from file
myFile_mee= open('myfile.txt','r+')
text=myFile_mee.read(100)
print(text) 