class Guest:
    def __init__(self, name, wallet, fav_song, intoxication):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.intoxication = intoxication

    def pay(self, amount):
        if self.wallet < amount:
            return False
        self.wallet -= amount
        return True

    def cheer(self):
        return "Woop!"

    def sing(self):
        # todo - call play_song from room obj
        # return the lyric string from the song
        # add lyric to song obj
        return "Lalalalalalalala!"

    def get_drunk(self, value):
        self.intoxication += value
