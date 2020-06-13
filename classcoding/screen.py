
from item import Items

class Screen():
    def __init__(self, MenuOption, ThankYouMessage, ErrorMessage, Item):
        self.MenuOption = MenuOption
        self.ThankYouMessage = ThankYouMessage
        self.ErrorMessage = ErrorMessage
        self.Item = Item
    
    def getMenuOption(self):
        return self.MenuOption

    def getThankYouMessage(self):
        return self.ThankYouMessage
    
    def getErrorMessage(self):
        return self.ErrorMessage

    def getItem(self):
        return self.Item
