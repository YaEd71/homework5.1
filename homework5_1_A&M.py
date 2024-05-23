class House:
    def __init__(self, numberOfFoors, currentFloor):
        self.numberOfFoors = numberOfFoors
        self.currentFloor = currentFloor

numberOfFoors = 0
while numberOfFoors <= 9:
    numberOfFoors += 1
    currentFloor = numberOfFoors
    print("Текущий этаж равен", numberOfFoors)

numberOfFoors = 10
while numberOfFoors > 1:
    numberOfFoors -= 1
    currentFloor = numberOfFoors
    print("Текущий этаж равен", numberOfFoors)

numberOfFoors = House
currentFloor = House