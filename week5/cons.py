# basic class constructor

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

dog = Dog("joe", "mama")
print(dog.name, dog.breed)
