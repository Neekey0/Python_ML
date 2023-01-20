class Laptop:
    def __init__(self,operating_system,memory):
     self.operating_system=operating_system
     self.memory=memory
    
    def get_laptop_name(self):
        return self.operating_system
        return self.memory

a=Laptop("Mac","8")
print(a.get_laptop_name())