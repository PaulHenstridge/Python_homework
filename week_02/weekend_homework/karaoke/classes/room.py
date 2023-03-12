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
    ):
        self.id = id
        self.capacity = capacity
        self.guests = guests
        self.current_song = current_song
        self.available_songs = available_songs
        self.extra_songs = extra_songs
        self.alcobot = alcobot
        self.takings = 0
        self._entry_fee = 10

    def check_in(self, guest, current_guests):
        if len(current_guests) >= self.capacity:
            return "sorry, room is full"
        if guest.can_pay(self._entry_fee):
            guest.pay(self._entry_fee)
            self.accept_payment(self._entry_fee)

            self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)

    def accept_payment(self, amount):
        self.takings += amount

    def play_song(self, song):
        # check if song is in list
        # return lyrics of song
        pass

    def purchase_extra_songs(self, extra_songs):
        # add extra songs to available_songs
        pass

    def sell_drink(self, alcobot, guest, drink_name):
        price = [drink.price for drink in alcobot.drinks if drink.name == drink_name]
        strength = [
            drink.alco_level for drink in alcobot.drinks if drink.name == drink_name
        ]
        if guest.can_pay(price[0]) and alcobot.breathalize(guest):
            drink = alcobot.sell_drink(guest, drink_name)
            guest.get_drunk(strength[0])
            return drink
        else:
            return "Sorry, no service"

    def end_session(self):
        pass
