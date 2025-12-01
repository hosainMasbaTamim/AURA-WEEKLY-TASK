# basic class and object 

# class
class Car:
    def __init__(self, brand, model):   # constructor
        self.brand = brand      
        self.model = model

    def show(self):                     # class function
        print(f"Car: {self.brand} {self.model}")

# objects
car1 = Car("x", "12")
car2 = Car("y", "11")

car1.show()
car2.show()
