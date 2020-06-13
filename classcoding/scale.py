from item import Items

class Scale():
    def __init__(self, WeightItem, Items):
        self.WeightItem = WeightItem
        self.Items = Items

    def getWeightItem(self):
        return self.WeightItem

    def getItems(self):
        return self.Items