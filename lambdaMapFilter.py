
#lambda  , it is an one line function

double = lambda x : x*2
add = lambda x,y: x+y
product = lambda x,y,z : x*y*z

print('double value by lambda method =',double(2))
print('sum by lambda method =',add(9,15))
print('product by lambda method =',product(5,6,7))

# MAP , we can map by using fuction and a iteratable value

a=(1,2,3,4,5,6,7,8,9)
b=(9,8,7,6,5,4,4)
z= map(lambda x:x*2,list(a))
print(list(z))
y=map(lambda x,y:x+y,a,b)
print(list(y))

# FILTER keyword is use to filter the data in a iterateable value container

d=filter(lambda x:x>5,a)
print(list(d))