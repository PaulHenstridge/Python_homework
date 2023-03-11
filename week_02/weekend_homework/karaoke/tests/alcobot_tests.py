import unittest
from classes.alcobot import Alcobot
from classes.drink import Drink
from classes.guest import Guest


class TestAlcobot(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Beer", 5, 2)
        self.drink2 = Drink("Sake", 6, 4)
        self.drinks_list = {self.drink1, self.drink2}

        self.guest1 = Guest("Bob Loblaw", 100, "I fought the law", 0)
        self.guest2 = Guest("Stove Jeebs", 0, "lalalala", 20)

        self.bot1 = Alcobot(666, 100, self.drinks_list)

    def test_can_sell_drink(self):
        self.bot1.sell_drink(self.guest1, "Beer")
        self.assertEqual(105, self.bot1.till)
        self.assertEqual(1, self.bot1.drinks_sold)

        # update numbers & return a drink
