from abc import ABC, abstractmethod

class Messenger(ABC):

    @abstractmethod
    def send_message(self):
        pass

    @abstractmethod
    def receive_message(self):
        pass


# Subclass implementing abstract methods
class FMessenger(Messenger):

    def send_message(self):
        print("I am sending message using Facebook")

    def receive_message(self):
        print("I am receiving message using Facebook")


# Object creation (cannot create object of abstract class)
m = FMessenger()

# Method calls
m.send_message()
m.receive_message()
