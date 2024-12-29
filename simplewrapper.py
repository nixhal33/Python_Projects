def simple_decorator(func):
    def wrapper():
        func()
        print("I’m doing something after the function!")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello, world!")

say_hello()
# @simple_decorator wraps the say_hello() function.
# When you call say_hello(), it doesn’t just print "Hello, world!" anymore. It also does the extra work added in the wrapper().

