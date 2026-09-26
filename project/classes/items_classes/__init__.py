class Items:
    item_count = 0
    def __init__(self, name, voltage, weight, matter):
        
        self.name = name
        self.voltage = voltage
        self.weight = weight
        self.matter = matter
        if weight == "N/A":
            Items.item_count += 1

class RoadsideItems:
    def __init__(self):
        self.items = []
        self.total_weight = 0
        self.non_magnetic_items = 0

    def collectNprint(self, item):
            self.items.append(item)
            print(f"{item.name} added to the net")
            if item.weight != "N/A":
                self.total_weight += item.weight
            else:
                self.non_magnetic_items += 1


    def view_inventory(self):
        if self.non_magnetic_items <= 1:
            print(f" has {self.non_magnetic_items} non-magnetic item and {self.total_weight}g of Iron:")
        else:
            print(f" has {self.non_magnetic_items} non-magnetic items and {self.total_weight}g of Iron:")
        for item in self.items:
            if item.weight == "N/A":
                print(f"• {item.name}")
            else:
                print(f"• {item.name}: {item.weight}g")

class BeachItems(RoadsideItems):
    def __init__(self):
        super().__init__()

    def collectNprint(self, item):
        super().collectNprint(item)

    def total_weight(self, item):
        super().total_weight(item)
    
    def view_inventory(self):
        super().view_inventory()

class LakeItems(RoadsideItems):
    def __init__(self):
        super().__init__()

    def collectNprint(self, item):
        super().collectNprint(item)

    def total_weight(self, item):
        super().total_weight(item)
    
    def view_inventory(self):
        super().view_inventory()