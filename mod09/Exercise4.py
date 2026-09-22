import random
class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed <= 0:
            self.current_speed = 0
            
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def race(cars):
    finish_line = False
    while not finish_line:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                finish_line = True
    return cars