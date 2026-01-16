class Vehicle():

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print("test: ",self.name)
        print("test: ",self.max_speed)
        print("test: ",self.mileage)

class Child(Vehicle):
    pass

objC = Child("stuff","test","idk")

objC.display()