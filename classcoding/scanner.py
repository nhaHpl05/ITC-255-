from item import Items

class Scanner():
    def __init__(self,Items, Membershipcard):
        self.Items = Items
        self.Membershipcard = Membershipcard

    def getItem(self):
        return self.Items

    def getMembershipcard(self):
        return self.Membershipcard

    

    
    