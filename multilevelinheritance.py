class Messenger:
    def send_message(self):
        print("Sending message")
    def receive_message(self):
        print("Receiving message")
class FacebookMessenger(Messenger):
    def send_message(self):
        print("Sending message using Facebook")
    def receive_message(self):
        print("Receiving message using Facebook")
class WhatsAppMessenger(Messenger):
    def send_message(self):
        print("Sending message using WhatsApp")
    def receive_message(self):
        print("Receiving message using WhatsApp")
def display(ref):
    ref.send_message()
    ref.receive_message()
F = FacebookMessenger()
W = WhatsAppMessenger()
display(F)
display(W)
