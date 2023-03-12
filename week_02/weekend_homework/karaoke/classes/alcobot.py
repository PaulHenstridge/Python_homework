class Alcobot:
    def __init__(self, id, till, drinks):
        self.id = id
        self.till = till
        self.drinks = drinks
        self.drinks_sold = 0
        self.alco_limit = 15

    def sell_drink(self, guest, drink_name):
        if self.breathalize(guest):
            for drink in self.drinks:
                if drink.name == drink_name:
                    if guest.can_pay(drink.price):
                        guest.pay(drink.price)
                        self.till += drink.price
                        self.drinks_sold += 1
                        return drink
            return f"{drink_name} is not available"
        return f"You are a level {guest.intoxication} drunk! No more booze!"

    def breathalize(self, guest):
        return guest.intoxication < self.alco_limit

    def tell_joke(self):
        pass
