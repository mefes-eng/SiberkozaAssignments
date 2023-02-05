# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

from os import name
from typing import Self


class user_mee:
    #constructor
    def __init__(self, name, email, age):
    Self.name=name # i cant understand here
    self.email=email 
    self.age=age

def greeting(self):
    return f'My name is{self.name}and I am {self.age}'

def has_birthday(self):
    self_age += 1
    
    #extend class
    class Customer(User):
    #constructor
def __init__(self, name, email, age):
    self.name=name
    self.email=email 
    self.age=age
    self.balance=0

def set_balance(self,balance):
    self.balance = balance

def greeting(self):
    return f'My name is{self.name}and I am {self.age} and my balance is{self.balance}'


    
    #init user object
    efe=User('efe elmas','efe@gmail.com',37)
    #init customer object
    mami=Customer('Mami Johnson','mami@yahoo.com',25)
    
    mami.set_balance(500)
    print(mami.greeting())
    
    efe.has_birthday
    print(efe.greeting()) 