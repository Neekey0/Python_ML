class counter:
    def __init__(self,num):
        self.num= num
        
    def add(self,value):
        self.num +=value
        return self.num
        
    def sub(self,value):
        self.num -=value
        return self.num
        
    #
  
         
counter1=counter(0)
print(counter1.add(3))
print(counter1.add(6))
print(counter1.add(9))

counter2=counter(10)
print(counter2.sub(5))