
#TODO: can have a list and for loop to display list contents
#TODO: use assosiation or inheritence to append stuff in list
#TODO: use Class variable to see how many items have been created
class AllNet:
    item_count = 0
    all_net = []
    def __init__(self, name, voltage):
        AllNet.all_net.append(self)
        self.name = name
        self.voltage = voltage
        self.weight = 0
        self.matter = 0

    def collect_print(self):
        print(f"{self.name}: {self.voltage} {self.weight} {self.matter}")

class RoadsideNet(AllNet):
    def __init__(self, name, voltage,):
        super().__init__(name, voltage)

class BeachNet(AllNet):
    def __init__(self, name, voltage,):
        super().__init__(name, voltage)

class LakeNet(AllNet):
    def __init__(self, name, voltage,):
        super().__init__(name, voltage)


roadside_net, beach_net, lake_net = [], [], []

roadside_net.append(RoadsideNet("ring", 130))
roadside_net.append(RoadsideNet("tin", 10))
roadside_net.append(RoadsideNet("nail", 41))

print(AllNet.item_count)
for item in roadside_net:
    item.collect_print()

for item in AllNet.all_net:
    item.collect_print()