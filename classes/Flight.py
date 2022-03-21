class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [ ]

    def add_passenger(self, name):
        print(F"{name}, tries to book a seat...")
        if not self.open_seats():
            print(F"No more seats available... sorry for {name}")
        else:
            self.passengers.append(name)
            print(f"{name}, just booked a seat!")
        print(F"End of session \n")

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
flight.add_passenger("George")
flight.add_passenger("Bob")
flight.add_passenger("Mary")
flight.add_passenger("Jose")
