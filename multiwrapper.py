def new_decorator(func):
    def wrapper():
        func()
        return "This is my hoe!"
    return wrapper

@new_decorator
def using_decorator():
    print("Imma money and a staaar!!")

using_decorator()
