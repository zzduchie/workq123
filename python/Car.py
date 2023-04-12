class Car:
    def __init__(self, make, model, year ):
        self.make=make
        self.model=model
        self.year=year
    def printCar(self):
        print("This is ",self.model, " by ", self.make, "launched in", self.year)

    def setModel(self, model):
        self.model=model
    
    def getModel(self):
        return self.model

make= input("Please enter the make of the car")
model= input("Please enter the model of the car")
year= input("Please enter the year of the car")


c1= Car(make, model, year)

c1.printCar()

