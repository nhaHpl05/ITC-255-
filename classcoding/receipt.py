from item import Items

class Receipt():
    def __init__(self, Template, Items, Tax, Discount):
        self.Template = Template
        self.Items = Items
        self.Tax = Tax
        self.Discount = Discount
    
    def getTemplate(self):
        return self.Template

    def getItems(self):
        return self.Items

    def getTax(self):
        return self.Tax

    def getDiscount(self):
        return self.Discount

    def __str__(self):
        return self.Template