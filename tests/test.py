import unittest
from item import Items
from scale import Scale
from sale import Sale

class ItemsTest(unittest.TestCase):
    def setUp(self):
        self.item=Items('2.50', 'snicker', '24906023')

    def test_price(self):
        self.assertEqual(str(self.item), '2.50')

    def test_name(self):
        self.assertEqual(str(self.item.getItemName), 'snicker')

    def test_Item_code(self):
        self.assertEqual(str(self.item.getItemCode), '24906023')

class ScaleTEst(unittest.TestCase):
    def setUp(self):
        self.scale = Scale('0','1.34', 'chicken')

    def test_get_Status(self):
        self.assertEqual(str(self.status), '0 ')

    def test_Item_Weight(self):
        self.assertEqual(str(self.Item_Weight), '1.34 ')
    
    def test_Item(self):
        self.assertEqual(str(self.Item), 'chicken')

class SaleTest(unittest.TestCase):
    def setUp(self):
        self.sale = Sale('1123', '1.34', 'chicken')
    
    def test_Sale_Number(self):
        self.assertEqual(str(self.SaleNumber), '1123')

    def test_Sale_price(self):
        self.assertEqual(str(self.SalePrice))

    def test_get_Items(self):
        self.assertEqual(str(self.getItems), 'chicken')
    


    