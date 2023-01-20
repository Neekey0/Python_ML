def calcu(*args):
    length=len(args)
    mul=1
    add=0
    if length<=2:
        for i in args:
            mul=mul*i
        return mul
    else:
        for i in args:
            add=add+i
        return add

print("Multiplications:",calcu())
print("Multiplication of(1,2):",calcu(1,2))
print("Multiplication of (2,3):",calcu(2,3))
print("Multiplication of (2):",calcu(2))
print("Addition between (2,3,4):",calcu(2,3,4))
print("Addition between (3,4,5,6):",calcu(3,4,5,6))
print("Addition between (5,6,7,8,9,10):",calcu(5,6,7,8,9,10))