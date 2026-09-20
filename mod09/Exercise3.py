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
            
car1 = Car("ABC-123", 142)
car1.drive(1.5)