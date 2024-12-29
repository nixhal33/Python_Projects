def repeat(times):
    def decor(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decor

@repeat(3) # here it means that hey decor please  repeat the function 3 times.
def greet():
    print("Hello Nix, How are you ?")

greet() 

class Multiply():

    @staticmethod
    def into(a,b):
        return a*b

    def notinto(self, a,b):
        return a+b

# and also calling the method into after declaring it as a static method
# calling method without creating an object
# this is how to access the static method 
print("result",Multiply.into(10,5))


# first object accessing the notinto method and it is also non static so i can access it many times using new objects
new_notinto=Multiply()
result=new_notinto.notinto(10,5)
print('The addition result: ',result)

# creating second object and accessing the notinto method
newone=Multiply()
result1=newone.notinto(100,100)
print("Another addition is : ",result1)



