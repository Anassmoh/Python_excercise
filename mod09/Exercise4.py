import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.license_plate = reg_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 2000

    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive(self, hour):
        self.travelled_distance += hour * self.current_speed

def race(cars):
    finish_line = False
    while not finish_line:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                finish_line = True
    return cars

car1 = Car("ABC-123", 142)
car2 = Car("ABC-222", 100)
cars = [car1, car2]

finish = race(cars)