class MetalFound:
    def __init__(self, name, voltage):
        self.name = name
        self.voltage = voltage
        self.weight = 0
        self.matter = 0

class AllFound:
    def __init__(self):
        self.net = []    

    def collect(self, item):
        self.net.append(item)

class RoadsideFound:
    def __init__(self):
        self.net = []    
    def collect(self, item):
        self.net.append(item)

class BeachFound:
    def __init__(self):
        self.net = []
    def collect(self, item):
        self.net.append(item)

class LakeFound:
    def __init__(self):
        self.net = []    
    def collect(self, item):
        self.net.append(item)


item1 = MetalFound("ring", 20)
item1.matter = "gold"
item1.weight = item1.voltage * 15
print("Item added to the net!\n")
print(f"{item1.name}  {item1.voltage} {item1.weight} {item1.matter}")

all = AllFound()
all.collect(item1)
print(all.net[0].name)