class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor
        
    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor > floor:
                self.floor_down()
            else:
                self.floor_up()
        
    def floor_up(self):
        self.current_floor += 1
        
    def floor_down(self):
        self.current_floor -= 1

class Building:
    def __init__(self, bottom_floor, top_floor, elevator):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator = elevator
        self.elevators = []
        for num in self.elevator:
            num.elevators.append(Elevator(bottom_floor, top_floor))
            
    
    def run_elevator(self, elevator, floor):
        self.elevators[elevator].go_to_floor(floor)