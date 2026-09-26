
#TODO: can have a list and for loop to display list contents
#TODO: use assosiation or inheritence to append stuff in list
#TODO: use Class variable to see how many items have been created
class Items:
    item_count = 0
    all_net = []
    def __init__(self, name, voltage, weight, matter):
        
        self.name = name
        self.voltage = voltage
        self.weight = weight
        self.matter = matter
        Items.all_net.append(self)
        Items.item_count += 1

class RoadsideItems:
    def __init__(self):
        self.items = []

    def collectNprint(self, item):
            self.items.append(item)
            print(f"{item.name} added to the net")

    def view_inventory(self):
        for item in self.items:
            print(item.name)

class BeachItems(RoadsideItems):
    def __init__(self):
        super().__init__()

    def collectNprint(self, item):
        super().collectNprint(item)
    
    def view_inventory(self):
        super().view_inventory()

class LakeItems(RoadsideItems):
    def __init__(self):
        super().__init__()

    def collectNprint(self, item):
        super().collectNprint(item)
    
    def view_inventory(self):
        super().view_inventory()

item1 = Items("ring", 130, 0, 0)
item2 = Items("tin", 10, 0, 0)
item3 = Items("nail", 41, 0, 0)

roadside_net = RoadsideItems()
beach_net = BeachItems()
lake_net = LakeItems()



roadside_net.collectNprint(item1)
roadside_net.collectNprint(item2)
beach_net.collectNprint(item2)
lake_net.collectNprint(item3)


roadside_net.view_inventory()
beach_net.view_inventory()
lake_net.view_inventory()


print(Items.item_count)
for item in  Items.all_net:
    print(item.name)



