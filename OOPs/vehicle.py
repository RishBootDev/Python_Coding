class Vehicle:
    def accelerate(self):
        print("The vehicle accelerates.")


class Car(Vehicle):
    def __init__(self, initial_speed):
        super().__init__()
        self.speed = initial_speed

    def accelerate(self):
        self.speed += 10
        print(f"The car accelerates. Current speed: {self.speed} km/h")


class Bicycle(Vehicle):
    def __init__(self, initial_speed):
        super().__init__()
        self.speed = initial_speed

    def accelerate(self):
        self.speed += 5
        print(f"The bicycle accelerates. Current speed: {self.speed} km/h")



car = Car(20)  # Initial speed of the car is 20 km/h
bicycle = Bicycle(15)  # Initial speed of the bicycle is 15 km/h

car.accelerate()  # Accelerate the car
bicycle.accelerate()  # Accelerate the bicycle

