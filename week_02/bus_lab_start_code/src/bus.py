class Bus:

    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = 0


    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return self.passengers
        
    def pick_up(self, person):
        self.passengers += 1

    def drop_off(self, person):
        self.passengers -= 1

    def empty_bus(self):
        self.passengers = 0

    def pick_up_from_stop(self, bus_stop):
        self.passengers += len(bus_stop.queue)