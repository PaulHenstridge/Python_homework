import unittest
from classes.guest import Guest


class Test_guest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Bob Loblaw", 100, "I fought the law", 0)
        self.guest2 = Guest("Stove Jeebs", 0, "lalalala", 20)

    def test_guest_has_name(self):
        self.assertEqual("Bob Loblaw", self.guest1.name)

    def test_guest_can_pay(self):
        self.guest1.pay(10)
        self.assertEqual(90, self.guest1.wallet)

    def test_guest_can_pay__insufficient_funds(self):
        self.assertEqual(False, self.guest2.can_pay(10))

    def test_guest_can_cheer(self):
        self.assertEqual("Woop!", self.guest1.cheer())

    def test_guest_can_sing(self):
        self.assertEqual("Lalalalalalalala!", self.guest1.sing())

    def test_guest_becomes_intoxicated(self):
        self.guest1.get_drunk(2)
        self.assertEqual(2, self.guest1.intoxication)
