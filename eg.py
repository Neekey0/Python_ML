input='@N1M@L'
letterCount=0
numberCount=0
specialCount=0
for i in input:
    #print(i)
    if i.isalpha():
        letterCount+=1
    elif i.isdigit():
        numberCount+=1
    else:
        specialCount+=1
        
print('Letter Count:',letterCount)
print('Number Count:',numberCount)
print('Special Count:',specialCount)
print('************')


list=[[1,-1,-1],[-1,1,-1],[-1,-1,1]]
#print(list)
sum=0
for i in list:
    index1=list.index(i)
    print(list[index1][index1])
   # print(i)
    for j in i:
       # print(j)
        index2=i.index(j)
        if (index1==index2):
            #print(j)
            sum=sum+j
            
print("Sum:",sum)
