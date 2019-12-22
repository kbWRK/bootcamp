class ElectricCar:
    def __init__(self, maxrange, ):
        self.maxrange = maxrange
        self.distance = maxrange

    def drive(self, distance):
        if self.distance < distance:
            return f"nie starczy ci paliwa przejechałes {self.distance}"
        else:
            self.distance -= distance
            return f"możesz przejechac {self.distance}"

    def charge(self, power):
        distance = self.distance
        if (self.distance + power) > self.maxrange:
            return f"nie przelewaj zatankowałes do {distance + power} a masz pojemnosc {self.maxrange} twój bak jest pełen "
        else:
            self.distance += power
            return f"zatankowałes do {self.distance}"


if __name__ == "__main__":
    car = ElectricCar(10)
    print(car.drive(70))
    print(car.charge(30))
    print(car.charge(50))