class Car:
    def __init__(self):
        self.licensePlate = "Unknown"

    def getlicensePlate(self):
        return self.licensePlate


car = Car()
print(car.getlicensePlate())