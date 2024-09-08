class Employee:
    name="yash"
    age=19
    salary=50000
    
    def __init__(self, *args, **kwargs):
        print(" i am creating an object")
    def getinfo(self):
        return(f"name {self.name} age {self.age} salary{self.salary}")
    @staticmethod
    def getstaticinfo():
        return ("hello")
    #  return(f"name {name} age {age} salary{salary}")//can not excute name 
yash= Employee()
print(yash.getinfo())

print(yash.name,yash.age,yash.salary)


# in oop of python it passes the self if we call yash.getinfo then it will do like Employee.getinfo(yash)


#-----------------static method---------------- then no need of self
print(yash.getstaticinfo())
# Unlike instance and class methods, static methods cannot access class attributes or instance attributes. In Python, we create a static method using a decorator. We write @staticmethod right above the method we want to decorate. Static methods have no implicit first argument.
