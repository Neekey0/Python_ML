class MyClass():
    college='nagarjuna'
    def __init__(self,name,depart):
        self.name= name 
        self.depart=depart
        
    def getName(self):
        return self.name
    
newClass=MyClass('Niki','CSIT') #newClass
# print(newClass.name)
# print(newClass.depart)
MyClass.college="Ism"

print(newClass.college)
print(newClass.getName())

newClass1=MyClass("Sthaa","IT")
print(newClass1.depart)
print(newClass1.college)
