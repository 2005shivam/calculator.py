def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("enter a option:-")
print("1.add\n2.subtract\n3.multiply\n4.divide")
choice=int(input("enter your option:"))
a=int(input("enter first num:"))
b=int(input("enter second num:"))
if(choice==1):
    print("add of",a,"and",b,"is",add(a,b))
elif(choice==2):
    print("subtract of",a,"and",b,"is",sub(a,b))
elif(choice==3):
    print("multiply of",a,"and",b,"is",mul(a,b))
elif(choice==4):
    print("divide of",a,"and",b,"is",div(a,b))

