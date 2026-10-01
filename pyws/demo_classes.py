def multiply(x, y):
    return x * y


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# instantiate
my_object = Rectangle(10, 20)
# print(my_object.width)
# print(my_object.area())

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"balance is: {self.balance}")

account = BankAccount("Jesse")
account.deposit(100)
account.show_balance()


class Base:
    pass


class Derived(Base):
    pass


class Vehicle:
    description = "This is a vehicle"

    def drive(self):
        return "Let's go"

    def brake(self):
        return "Braking"


class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

car = Car()
print(car.description)
print(car.drive())

truck = Truck()
print(truck.brake())