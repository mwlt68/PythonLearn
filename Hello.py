print("Hello python")
# this is command line different  from c# or java

# if structure

x=3;
if x > 2:
    print("X is bigger then 2 ");

# dynamically  types

myFloat=7.0
print(myFloat);
myFloat="float"
print(myFloat)
myFloat="10.3"
print(float(myFloat))

myInt=2
myString="text"
    # print(myInt+myString) =>  TypeError: unsupported operand type(s) for +: 'int' and 'str'

a,b,c=1,"asd",5.3
print(a,b,c)

# None keyword like null in c language
z=None
print(z)
z=2
if isinstance(z,int):
    print("z is int")

# Declare an array
array=[]
array.append(2)
array.append(3)
array.append(4)

#  this for structure like c# foreach structure
for a in array:
    print(a)

# Easy mathematical operands
squared=3**2
cubed=5**3
print(squared);print(cubed)

# Easy sum,multiply an array

arr1=[1,2,3]
arr2=[4,5]
print(arr1+arr2)
#----------------------------------------------------------------
strArray=["hello"]*10
print(strArray)
#----------------------------------------------------------------
strArray=["hello"]*2  + [2]* 4
print(strArray)

#Python uses C-style string formatting to create new, formatted strings.
name="Mevlüt"
age=21
print("Name:%s  Age:%d" % (name,age))

#Basic string operands
str="my string length"
print(len(str))
#----------------------------------------------------------------
print(str.index('en'))
#----------------------------------------------------------------
print(str.count('t'))
#----------------------------------------------------------------
print(str[3:9])  # [start Index, stop Index]
#----------------------------------------------------------------
print(str[3:9:2]) # [start Index, stop Index,Step]
#----------------------------------------------------------------
print(str[::-1]) # reverse of string
#----------------------------------------------------------------
print(str.upper())
#----------------------------------------------------------------
print(str.lower())
#----------------------------------------------------------------
print(str.startswith("my"))
#----------------------------------------------------------------
print(str.endswith("eth"))
#----------------------------------------------------------------
print(str.split(' '))


# Condition
x=2
print(x==2)
print(x==3)

#----------------------------------------------------------------
name="Mevlüt"
age = 21
if  name=="Mevlüt" or name=="Ali":
    print("You are Mevlüt or Ali")
if  name=="Mevlüt" and age==21:
    print("I met you")

#----------------------------------------------------------------
nameList=["Mevlüt","Ali","Ahmet"]
if  "Ali" in nameList:
    print("Ali name is in name list")

#----------------------------------------------------------------
statement1=False;
statement2=True;

if  statement1 is True:
    # do something
    pass
elif statement2 is False:
    # do something
    pass
else:
    print("Else")

#----------------------------------------------------------------
x=[1,2,3]; y=[1,2,3]
print(x==y)
print(x is y)

# Loops

for x in range(4):
    print(x)
for x in range(4,6):
    print(x)
for x in range(4,15,3):
    print(x)

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))