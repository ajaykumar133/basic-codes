from threading import *                           # importing thread module

class hlo(Thread):                                 # inherit the class in which you want to use threding
    def run(self):                                 # run is a mtd in thread class , so we need to define run mtd for threading
        for i in range(500):
            print('hello ')

class hi(Thread):
    def run(self):
        for i in range(500):
            print('hii ')

obj1 = hlo()
obj2 = hi()

obj1.start()                                    #to start a thread we call start mtd , and now it will implicitly call the run() by itself
obj2.start()
