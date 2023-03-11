import unittest
from classes.alcobot import Alcobot
from classes.drink import Drink
from classes.guest import Guest
from classes.get_joke import MakeApiCall


class TestAlcobot(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Beer", 5, 2)
        self.drink2 = Drink("Sake", 6, 4)
        self.drinks_list = {self.drink1, self.drink2}

        self.guest1 = Guest("Bob Loblaw", 100, "I fought the law", 0)
        self.guest2 = Guest("Stove Jeebs", 0, "lalalala", 20)

        self.get_jokes = MakeApiCall("https://icanhazdadjoke.com/")

        self.bot1 = Alcobot(666, 100, self.drinks_list)

    def test_can_sell_drink(self):
        self.bot1.sell_drink(self.guest1, "Beer")
        self.assertEqual(105, self.bot1.till)
        self.assertEqual(1, self.bot1.drinks_sold)
        # check that passing a string returns a Drink obj
        self.assertEqual(self.drink2, self.bot1.sell_drink(self.guest1, "Sake"))

    def test_breathalize__pass(self):
        self.assertEqual(True, self.bot1.breathalize(self.guest1))

    def test_breathalize__fail(self):
        self.assertEqual(False, self.bot1.breathalize(self.guest2))

    def test_drunk_guest_refused_service(self):
        response = self.bot1.sell_drink(self.guest2, "Sake")
        self.assertEqual("You are a level 20 drunk! No more booze!", response)

    def test_can_tell_joke(self):
        joke = self.get_jokes.get_data()
        self.assertIsNotNone(joke)
