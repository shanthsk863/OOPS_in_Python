class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object of Car class
my_car = Car("Toyota", "Corolla")
my_car.display_info()
