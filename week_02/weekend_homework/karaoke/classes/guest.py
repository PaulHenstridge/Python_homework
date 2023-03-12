class Guest:
    def __init__(self, name, wallet, fav_song, intoxication):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.intoxication = intoxication

    def can_pay(self, amount):
        return self.wallet > amount

    def pay(self, amount):
        self.wallet -= amount

    def cheer(self):
        return "Woop!"

    def sing(self):
        # todo - call play_song from room obj
        # return the lyric string from the song
        # add lyric to song obj
        return "Lalalalalalalala!"

    def get_drunk(self, value):
        self.intoxication += value
