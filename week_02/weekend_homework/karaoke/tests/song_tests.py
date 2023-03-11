import unittest

from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Woowoowoo", "The Woo", 200)

    def test_song_has_name(self):
        self.assertEqual("Woowoowoo", self.song1.title)
