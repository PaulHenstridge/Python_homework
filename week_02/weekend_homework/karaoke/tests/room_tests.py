import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.alcobot import Alcobot
from classes.drink import Drink


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Bob Loblaw", 100, "I fought the law", 0)
        self.guest2 = Guest("Stove Jeebs", 0, "lalalala", 20)
        self.group1 = [self.guest1, self.guest2]
        self.group2 = [
            self.guest1,
            self.guest2,
            self.guest1,
            self.guest2,
            self.guest1,
            self.guest2,
            self.guest1,
            self.guest2,
        ]
        self.song1 = Song("Woowoowoo", "The Woo", 200)
        self.song2 = Song("doopidoo", "The doo", 300)
        self.song_list1 = [self.song1, self.song2]
        self.song_list2 = [self.song1, self.song2, self.song1, self.song2]

        self.drink1 = Drink("Beer", 5, 2)
        self.drink2 = Drink("Sake", 6, 4)
        self.drinks_list = {self.drink1, self.drink2}
        self.bot1 = Alcobot(666, 100, self.drinks_list)

        self.room1 = Room(
            1,
            6,
            self.group1,
            self.song1,
            self.song_list1,
            self.song_list2,
            self.bot1,
        )

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room1.capacity)

    def test_check_in_guest(self):
        self.room1.check_in(self.guest1, self.group1)
        self.assertEqual(3, len(self.room1.guests))

    def test_check_in_guest__capacity_reached(self):
        self.assertEqual(
            "sorry, room is full", self.room1.check_in(self.guest1, self.group2)
        )

    def test_check_out_guest(self):
        self.room1.check_out(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_room_accepts_payment(self):
        self.room1.check_in(self.guest1, self.group1)
        self.assertEqual(10, self.room1.takings)
        self.assertEqual(90, self.guest1.wallet)

    def test_room_is_full(self):
        check_in_attempt = self.room1.check_in(self.guest1, self.group2)
        self.assertEqual("sorry, room is full", check_in_attempt)

    def test_display_takings(self):
        self.room1.check_in(self.guest1, self.group1)
        self.assertEqual(10, self.room1.takings)

    def test_sell_drink(self):
        response = self.room1.sell_drink(self.bot1, self.guest1, "Beer")
        self.assertEqual("Beer", response.name)

    def test_alcohol_gets_guest_drunk(self):
        self.room1.sell_drink(self.bot1, self.guest1, "Beer")
        self.assertEqual(2, self.guest1.intoxication)

    def test_sell_drink__guest_too_drunk(self):
        attempt_buy_drink = self.room1.sell_drink(self.bot1, self.guest2, "Beer")
        self.assertEqual("Sorry, no service", attempt_buy_drink)

    def test_add_extra_songs(self):
        pass

    def test_end_session(self):
        pass
