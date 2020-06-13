class Items():
    def __init__(self, ItemPrice, ItemName, ItemCode):
        self.ItemPrice = ItemPrice
        self.ItemName = ItemName
        self.ItemCode = ItemCode
    def getItemPrice(self):
        return self.ItemPrice

    def getItemName(self):
        return self.ItemName
    
    def getItemCode(self):
        return self.ItemCode

    def __str__(self):
        return self.ItemName