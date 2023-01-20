class Animal:
    def __init__(self,name):
        self.name=name
        
    def getAnimalName(self):
        
        print("Animal is :::",self.name)
        
ani=Animal("Mahes")
ani.getAnimalName()