class Car:

    def __init__(self,ym,m,s):
        self.__year_model = ym
        self.__make = m
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
