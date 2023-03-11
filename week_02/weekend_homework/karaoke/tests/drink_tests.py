import unittest
from classes.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Beer", 5, 2)
        self.drink2 = Drink("Sake", 6, 4)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink1.price)
