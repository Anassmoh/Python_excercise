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

    
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        
    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            
        
    def print_status(self):
        for i in range(len(self.cars)):
            print(f"{self.cars[i].license_plate} {self.cars[i].maximum_speed} {self.cars[i].current_speed} {self.cars[i].travelled_distance}")
        
    
    def race_finished(self):
        race_finished = False
        while not race_finished:
            self.hour_passes()
            for i in range(len(self.cars)):
                if self.cars[i].travelled_distance >= 10000:
                    race_finished = True
            return self.cars

cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")


for hour in range(5):
    race.hour_passes()
    if hour == 2:
        print(f"After {hour+1} hours, race finished: {race.race_finished()}")