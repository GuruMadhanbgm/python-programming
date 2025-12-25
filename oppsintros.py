class Bike:
    def __init__(self):
        self.name = "Honda"
        self.price = 2345657
        self.colour = "Black"

    def accelerate(self):
        print("Bike is accelerating")
        print("Colour:", self.colour)

    def brake_system(self):
        print("Bike is stopping")

    def start(self):
        print("Bike is starting")
b1 = Bike()
b1.start()
b1.accelerate()
b1.brake_system()
