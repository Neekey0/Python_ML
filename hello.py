def expression(a,b,c):
    return a*b*c
print(expression(2,4,5))

sumFunc=lambda a,b,c:a*b*c
print(sumFunc(3,3,3))


list=[0]*5
print(list)
list=[1,2]+[3,4]
print(list)
'''
list=[1,2,3,4,5]
a,b,c,d,e=list
a,*rest=list
*rest,val=list
a,*rest,b=list
print(a,rest)
print(a,rest,val)
print(c)
'''

list1=[1,2,3]
list1[1]=4
print(type(list1))

list2=(1,2,3)
print(type(list2))


def func(*args):
    sum=0
    for val in args:
        sum=sum+val
    return sum
print(func(2,4,6))

def product(*args):
    mul=1
    for val in args:
        mul=mul*val
    return mul
print(product())
print(product(2,3))
print(product(2,2,2,2))

a={'a':1,'b':2,'c':3}

d=dict(x=1,y=1)
for i in d.items():
    print(i)
print(a)
print(d)