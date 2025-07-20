# Intro to inheritance
class Parent:
    def __init__(self):
        self.eyes = "blue"
class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.age = 10
child = Child()
print(child.eyes)  # Output: blue
print(child.age)   # Output: 10

class Greeting:
    def greet(self):
        print("Hello from the parent class!")
class Person(Greeting):
    name = "Aayush"
p = Person()
p.greet()  # Output: Hello from the parent class!

class Car:
    def a(self):
        print("starting")
class HybridCar(Car):
    def b(self):
        print("stopping")
a = HybridCar()
a.a()  # Output: starting
a.b()  # Output: stopping