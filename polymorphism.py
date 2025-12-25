# Base class
class Messenger:
    def send_message(self):
        print("I am sending message")

    def receive_message(self):
        print("I am receiving message")


# Facebook Messenger
class FMessenger(Messenger):
    def send_message(self):
        print("I am sending message using Facebook")

    def receive_message(self):
        print("I am receiving message using Facebook")


# WhatsApp Messenger
class WMessenger(Messenger):
    def send_message(self):
        print("I am sending message using WhatsApp")

    def receive_message(self):
        print("I am receiving message using WhatsApp")

    def live_location(self):
        print("I am sharing live location using WhatsApp")


# Instagram Messenger
class IMessenger(Messenger):
    def send_message(self):
        print("I am sending message using Instagram")

    def receive_message(self):
        print("I am receiving message using Instagram")


# Polymorphism function
def display(ref):
    ref.send_message()
    ref.receive_message()

    # Extra feature only for WhatsApp
    if isinstance(ref, WMessenger):
        ref.live_location()


# Object creation
f = FMessenger()
w = WMessenger()
i = IMessenger()

# Function calls
display(f)
display(w)
display(i)
