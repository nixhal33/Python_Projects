def Add(fx):
    def wrapper(a,b):
        print("Addition of two numbers :")
        print(f"Adding {a} and {b}.....")
        return fx(a,b)
    return wrapper

@Add
def addition(a,b):
    return a+b

result=addition(123,234)
print("result: ",result)

