import math
import random

x=pow(5,8)  #this is going to find 5^8
print(x)

y= math.sqrt(x)     # this is going to find sqrt of no. x
print(y)

a='this is str a'
print(a+str(y))

#=======================   python list ==========================#

name=['abc','egf','ijk','xyz']

name.append('mno')
name.insert(4,'qrs')          # this will insert the value at a defined index value
print(name)

age=[12,23,34,45,54,65,45]

name.extend(age)                # merge 2 lists
age.sort()              #this will sort the list age
print(age[2:5])         #this will print value from indexValue 2 to 5 & operation is known as slice
print(age[2: ])         #will print indexs from 2 to last of list
print(age[:5])          #will print form index 0 to index 5
print(age[0:6:2])       #will print list from 0-6index but everytime skips 2 value(means print 0-2-4-6)
print(name)
print(name,age)         # this will print multiple lists in one time