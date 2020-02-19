#Function

def myFunction():
    print("Hello from my function")
myFunction()

def myFunction2(name, age):
    print("Your name is %s and your age is %d" % (name,age))
myFunction2("Mevlüt",21)

def sumFunc(val1,val2):
    return val1+val2
print(sumFunc(3,2))

# Class


class Vehicle:

    name=None
    price=None
    def description(self):
        print("This is %s.Price is %d " % (self.name,self.price))

car=Vehicle()
car.name="Toyota"
car.price=2000
car.description()

# Dictionaries
nameBook={}
nameBook['Ahmet']=0
nameBook['Ali']=1
nameBook['Veli']=2
# or you can use this nameBook={'ahmet':0,'Ali':1,'Veli':2}
print(nameBook)

for name,num in nameBook.items():
    print("Name is %s.Number is %d" % (name,num))

del nameBook["Ali"]
# or you can use nameBook.pop("Ali")

if  "Ahmet" in nameBook:
    print("Ahmet in name book")
if  not "Ali" in nameBook:
    print("Ali not in name book")

#Numpy arrays =>  are great alternatives to Python Lists

import numpy as np
weight_list=[80.5,74.2,49.7]
weight_array=np.array(weight_list)
weight_array*=2
print(weight_array)

# Pandas => is a high-level data manipulation tool developed
# DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
#-------------------------------------------
brics.index= ["BR", "RU", "IN", "CH", "SA"]
print(brics)
# You can read data from csv file
cars = pd.read_csv('cars.csv')
print(cars)
#Square brackets can also be used to access observations (rows) from a DataFrame.
print(cars[4:6])

