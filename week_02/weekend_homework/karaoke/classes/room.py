class Room:
    def __init__(
        self,
        id,
        capacity,
        guests,
        current_song,
        available_songs,
        extra_songs,
        alcobot,
        revenue,
    ):
        self.id = id
        self.capacity = capacity
        self.guests = guests
        self.current_song = current_song
        self.available_songs = available_songs
        self.extra_songs = extra_songs
        self.alcobot = alcobot

    def check_in(self, guest, current_guests):
        if len(current_guests) >= self.capacity:
            return "sorry, room is full"
        self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)

    def play_song(self, song):
        # check if song is in list
        # return lyrics of song
        pass

    def purchase_extra_songs(self, extra_songs):
        # add extra songs to available_songs
        pass

    def sell_drink(self, barbot, guest, drink):
        # call barbot.sell_drink(guest, drink)
        pass

    def end_session(self):
        pass
