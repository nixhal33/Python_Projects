def least_difference(a, b, c):
    d1=abs(a-b)
    d2=abs(b-c)
    d3=c-a
    return min(d1, d2, d3),max(d1,d2,d3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

