class Laptop:
    def __init__(self,operating_system,memory):
     self.operating_system=operating_system
     self.memory=memory
    
    def getLaptopName(self):
        return self.operating_system

a=Laptop("Mac","8 gb")
print(a.getLaptopName())