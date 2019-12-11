def my_list(list):
    for i in list:
        yield i         #yield is keyword for iteration in gen.             generators itself handles the exception

a=[1,0,3,6,5,3]
mylist=my_list(a)
                    #it will print as many no. as much times generators are called using next keyword
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))


