
class Items:
    all_count = 0
    
    def __init__(self, name, voltage, weight, matter):
        self.name = name
        self.voltage = voltage
        self.weight = weight
        self.matter = matter
        Items.all_count += 1
        return
        
class RoadsideItems:
    def __init__(self):
        self.items = []
        self.items_count = 0
        self.aluminium_weight = 0
        self.aluminium_price = 0
        self.brass_weight = 0
        self.brass_price  = 0
        self.copper_weight = 0
        self.copper_price  = 0
        self.iron_weight = 0
        self.iron_price = 0
        self.silver_weight = 0
        self.silver_price = 0
        self.gold_weight = 0
        self.gold_price = 0
        return

    def collectNprint(self, item):
            self.items.append(item)
            print(f"{item.name} is added to the net.")
            self.items_count += 1
            if item.matter == "aluminium":
                self.aluminium_weight += item.weight
                self.aluminium_price += (item.weight * 0.018)
            elif item.matter == "brass":
                self.brass_weight += item.weight
                self.brass_price += (item.weight * 0.066)
            elif item.matter == "copper":
                self.copper_weight += item.weight
                self.copper_price += (item.weight * 0.076)
            elif item.matter == "iron":
                self.iron_weight += item.weight
                self.iron_price += (item.weight * 0.002)
            elif item.matter == "silver":
                self.silver_weight += item.weight
                self.silver_price += (item.weight * 11)
            elif item.matter == "gold":
                self.gold_weight += item.weight
                self.gold_price += (item.weight * 720)
            return


    def view_inventory(self):
        if self.items_count <= 1:
            print(f" has {self.items_count} item:")
        else:
            print(f" has {self.items_count} items:")
        for item in self.items:
                print(f" •{item.name}: {item.weight}g")
        return

class BeachItems(RoadsideItems):
    def __init__(self):
        super().__init__()
        return

    def collectNprint(self, item):
        super().collectNprint(item)
        return
    
    def view_inventory(self):
        super().view_inventory()
        return

class LakeItems(RoadsideItems):
    def __init__(self):
        super().__init__()
        return

    def collectNprint(self, item):
        super().collectNprint(item)
        return
    
    def view_inventory(self):
        super().view_inventory()
        return