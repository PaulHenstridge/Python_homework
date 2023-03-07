class BusStop:

    def __init__(self, name):

        self.name = name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)
