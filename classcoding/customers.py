from scanner import Scanner
from item import Items

class Customer():
    def __init__(self,MembershipCard,Items,CreditCard,cash):
        self.MembershipCard = MembershipCard
        self.Items = Items
        self.CreditCard = CreditCard
        self.cash = cash

    def getMembershipCard(self):
        return self.getMembershipCard

    def getItems(self):
        return self.Items

    def getCreditCard(self):
        return self.CreditCard

    def getCash(self):
        return self.cash

    def __str__(self):
        return self.getMembershipCard