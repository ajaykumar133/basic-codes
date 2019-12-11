from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class square(shape):

    def __init__(self,side):
        #side=int(input('enter the side of square : '))
        self.side=side

    def area(self):
        a= self.side * self.side
        print('area = ',a)

    def perimeter(self):
        p= 4*self.side
        print('perimeter = ',p)

sq=square(7)

sq.area()
sq.perimeter()


