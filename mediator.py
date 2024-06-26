class Mediator:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_message(message, sender)

    def receive_message(self, message, sender):
        print(f"{sender.name} sent message: {message}")
        self.send_message(message, sender)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.register_user(self)

    def send_message(self, message):
        print(f"{self.name} sending message: {message}")
        self.mediator.receive_message(message, self)

    def receive_message(self, message, sender):
        print(f"{self.name} received message '{message}' from {sender.name}")


if __name__ == '__main__':
    my_mediator = Mediator()

    john = User("John", my_mediator)
    jane = User("Jane", my_mediator)

    john.send_message("Hello, Jane!")
    jane.send_message("Hello, John!")