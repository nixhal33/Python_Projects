# way of error handling or let's say exception handling
file=open('file.txt','w') 

try:
    file.write("This is my first exception")

finally:
    file.close

with open('file.txt','w') as file:
        file.write("This is a sample of exception handling")

