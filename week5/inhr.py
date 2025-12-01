# basic enharitance

class Cat:
    def speak(self):
        print("bark!")

class Car(Cat):         # inherits cat class
    pass

mew = Car()
mew.speak()