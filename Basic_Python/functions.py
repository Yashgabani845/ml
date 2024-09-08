def func1(surname,someone="gay"):
    name="your surname is "+surname
    if(surname=="ella"):
        name= name +"you are" + someone
    return (name)
print(func1(input("enter your name")))

#-----------------Recursion -------------
def fact (n):
    if(n==1):
        return n
    else :
        return n*fact(n-1)
    
print(fact(10))