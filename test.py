# if []:
#     print('if')
# elif '':
#     print('elif')
# else:
#     print('else')

# for i in range(0,10,2):
#     print(i)


# for i in range(0,100,3):
#     print(i)

# sum = 0
# for a in [1,2,3]:
#     sum += a 

# print(sum)

# sum=0
# for val in [1,2,3]:
#     sum1=0
#     sum=sum+1
# print(sum)
# print(sum1)
""" 
sum = 0
newsum=0
def summ(a,b):
    newsum = 2
    sum = sum + newsum 

summ(1,2)

"""


def multiply(a=1,b=1,c=1):   
    return a*b*c

print(multiply(1,2,3))
print(multiply(1,2,0))
print(multiply(1,2))
print(multiply(1))

def multi(*args):
    print(args)

multi(1,2)



sum = 0
newsum=0
def summ(a,b):
    global sum
    newsum = 4
    sum = sum + newsum 
    print (sum)
    print(newsum)
summ(3,2)
