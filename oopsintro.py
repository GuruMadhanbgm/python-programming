class Bike:
    def _init_(self):
        self.name = "honda"
        self.price = 2345657
        self.colour = "black"
    def accelerate(self):
        print("accelerating")
        print(self.colour)
    def breaksystem(self):
        print("bike is stopping")

    def start(self):
        print("bike is starting")
b1 = Bike()
b1.start()
b1.accelerate()
b1.breaksystem()
