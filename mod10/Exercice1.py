class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor
        
    
    def go_to_floor(self, number):
        while self.current_floor != number:
            if self.current_floor < number:
                self.floor_up()
            elif self.current_floor > number:
                self.floor_down()
            else:
                break
            
    def floor_up(self):
        self.current_floor += 1
        return
        
    def floor_down(self):
        self.current_floor -= 1
        return