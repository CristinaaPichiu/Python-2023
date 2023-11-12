class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, engine_efficiency, car_weight):
        super().__init__(make, model, year)
        self.engine_efficiency = engine_efficiency
        self.car_weight = car_weight

    def calculate_mileage(self):
        return (self.engine_efficiency * 100) / self.car_weight

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  # Miles per gallon (mpg)

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity  # Towing capacity in pounds

    def calculate_towing_capacity(self):
        return self.towing_capacity

if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 0.2, 1500)  # Example values for engine efficiency and weight
    print("Car mileage:", car.calculate_mileage())

    bike = Motorcycle("Harley Davidson", "Sportster", 2020, 50)  # Assume fuel efficiency is 50 mpg for the bike
    distance = 100
    print(f"Motorcycle mileage for {distance} miles:", bike.calculate_mileage(distance))

    truck = Truck("Ford", "F150", 2019, 10000)
    print("Towing capacity:", truck.calculate_towing_capacity())
