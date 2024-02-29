import CarClass as c

my_car = c.Car('','',0)

for count in range(5):
    my_car.accelerate()
    print(f"The speed of the car is {my_car.get_speed()}")
    print()

for count in range(5):
    my_car.brake()
    print(f"The speed of the car is {my_car.get_speed()}")
    print()
    




