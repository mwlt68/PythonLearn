import random as rnd

def getRandom():
    for i in range(6):
        yield rnd.randint(0,40)
for i in getRandom():
    print(i)

# Fibonacci example
def fibo():
    a,b=1,1
    while True:
        yield a
        a,b=b,a+b
counter = 0
for n in fibo():
    print(n)
    counter += 1
    if counter == 10:
        break

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
for x in words:
    print(x)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newList=[int(x) for x in numbers if x > 0]
print(newList)

# The "therest" variable is a list of variables, which receives all arguments
def myfunc(*manyInt):
    print(manyInt)

myfunc("a","sad",4)
# send functions arguments by keyword,
def keyword_printer(**keyList):
    print(keyList)
ing="english"
tr="turkish"
keyword_printer(ing="english",tr="turkish")

#try/except block.
list=[1,2,3,4]
try:
    for x in range(10):
        print(list[x])
except IndexError:
    print("There is an error !")
#Sets are lists with no duplicate entries.
#Since the rest of the sentence uses words which are already in the set, they are not inserted twice.
text="my name is Eric and Eric is my name"
set_text=set(text.split())
print(set_text)

#To find out which members attended both events, you may use the "intersection" method:
a=set(["Ali","Veli","Deli"])
b=set(["Mehmet","Veli"])
print(a.intersection(b))
print(a.union(b))
print(a.symmetric_difference(b))
print(a.difference(b))

# Nested function
def print_msg(number):
    def printer():
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)