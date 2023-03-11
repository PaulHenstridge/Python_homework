class Alcobot:
    def __init__(self, id, till, drinks):
        self.id = id
        self.till = till
        self.drinks = drinks
        self.drinks_sold = 0

    def sell_drink(self, guest, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                self.till += drink.price
                self.drinks_sold += 1
                return drink
        return f"{drink_name} is not available"

    def breathalize(self):
        pass

    def tell_joke(self):
        pass
