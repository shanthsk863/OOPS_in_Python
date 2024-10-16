class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def display_info(self):
        print(f"Car: {self.brand}, Horsepower: {self.engine.horsepower}")

engine = Engine(150)
car = Car("Honda", engine)
car.display_info()
