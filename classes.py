class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassengers(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True

    def openSeats(self):
        return (self.capacity - len(self.passengers))

flight = Flight(3)
people = ["Tom","Dick","Harry","Jane"]
for person in people:
    success = flight.addPassengers(person)
    if success:
        print("success")
    else:
        print("Fail")