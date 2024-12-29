a=[1,2,3,4,5,6,7,8]
def square(num):
    return (x**2 for x in num if x%2==0)

result=list(square(a))
print(result)

