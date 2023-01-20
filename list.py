def numbers():
    list=[]
    for i in range(4,31,2):
        #print(i)
        list.append(i)
        #print(i)
    #print(list)
    return list

print(numbers())

  
    

input=['ABC','','CDE','']
string=[x for x in input if len(x)>0]
print(string)