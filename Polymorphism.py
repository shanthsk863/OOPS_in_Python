class Bird:
    def fly(self):
        print("Bird is flying")

class Plane:
    def fly(self):
        print("Plane is flying")

def take_flight(entity):
    entity.fly()

bird = Bird()
plane = Plane()

take_flight(bird)   # Bird is flying
take_flight(plane)  # Plane is flying
