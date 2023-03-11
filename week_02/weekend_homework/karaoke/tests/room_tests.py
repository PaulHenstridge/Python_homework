import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


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

        self.room1 = Room(
            1,
            6,
            self.group1,
            self.song1,
            self.song_list1,
            self.song_list2,
            ["alcobot"],
            100,
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
        pass

    def test_display_revenue(self):
        pass

    def test_sell_drink(self):
        # call alcobot.sell_drink()
        pass

    def test_sell_drink__guest_intoxicated(self):
        pass

    def test_add_extra_songs(self):
        pass

    def test_end_session(self):
        pass
