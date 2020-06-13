from item import Items

class Sale():
    def __init__(self, SaleNumber, CashSale,CreditSale, Items):
        self.SaleNumber = SaleNumber
        self.CashSale = CashSale
        self.CreditSale = CreditSale
        self.Items = Items

    def getSaleNumber(self):
        return self.SaleNumber

    def getCashSale(self):
        return self.CashSale

    def getCreditSale(self):
        return self.CreditSale

    def getItems(self):
        return self.Items