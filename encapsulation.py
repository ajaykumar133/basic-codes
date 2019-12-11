class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200                  #defining values to private var
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))        # printing pvt. var


redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private //THIS IS SIMPLY A TEST TO CHK PVT VAR
redcar.drive()




