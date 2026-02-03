x=int(input("Enter x number: "))
y=int(input("Enter y number: "))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
def pow(x,y):
    return x**y
def sqrt(x):
    return x**(1/2)
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.mod")
print("6.power")
print("7.square root")
print("choose any one from  the above choices")
c=int(input("enter your choice: "))
if c==1:
    print(add(x,y))
elif c==2:
    print(sub(x,y))
elif c==3:
    print(mul(x,y))
elif c==4:
    print(div(x,y))
elif c==5:
    print(mod(x,y))
elif c==6:
    print(pow(x,y))
elif c==7:
    print(sqrt(x))
else:
    print("enter valid choice")
