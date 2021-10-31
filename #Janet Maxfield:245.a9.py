#245 assignment 9


class Vehicle:
    # Vehicle attributes
    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    # Get
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fuelType

    def getOptions(self):
        return self.options

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Color: {self.color}, FuelType: {self.fuelType}, Options: {self.options}"


# Car class
class Car(Vehicle):

    # Constructor
    def __init__(self, make, model, color, fuelType, options, EngineSize, numDoors):
        super().__init__(make, model, color, fuelType, options)  

        # Super class class
        # Initialize car's attributes
        self.engineSize = EngineSize
        self.numDoors = numDoors

    # Functions
    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors

    def __str__(self):
        return  "CAR:==> "+super(Car, self).__str__() + ", Engine Size " + str(self.engineSize) + ", NumDoors: " + str(self.numDoors)

    # Pickup class inherits from Vehicle


class Pickup(Vehicle):

    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        super().__init__(make, model, color, fuelType, options)  # Super class class
        # Initialize pickup's attributes
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    # Functions
    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength

    def __str__(self):
        return "PICKUP:==> "+super(Pickup, self).__str__() + ", Cab Style " + str(self.cabStyle) + ", Bed Length: " + str(self.bedLength)


# Test code 
if __name__ == '__main__':
    garage = [] 
    
    # Take empty virtual garage
    # Prepare some vehicles
    car1 = Car("MAKE1", "MODEL1", "RED", "PETROL", "OPTIONS1", "SIZE1", 4)
    car2 = Car("MAKE2", "MODEL2", "BLUE", "DIESEL", "OPTIONS2", "SIZE2", 2)
    car3 = Car("MAKE3", "MODEL3", "GREEN", "PETROL", "OPTIONS3", "SIZE3", 6)

    pickup1 = Pickup("MAKE4", "MODEL4", "RED", "PETROL", "OPTIONS4", "CAB STYLE1", "BED LENGTH1")
    pickup2 = Pickup("MAKE5", "MODEL5", "BLUE", "DIESEL", "OPTIONS5", "CAB STYLE2", "BED LENGTH2")
    pickup3 = Pickup("MAKE6", "MODEL6", "RED", "PETROL", "OPTIONS6", "CAB STYLE3", "BED LENGTH3")
    # Add some vehicles to garage
    garage = [car1, pickup2, pickup3, car2, car3, pickup1]

    # Print the garage
    for vehicle in garage:
        print(vehicle)