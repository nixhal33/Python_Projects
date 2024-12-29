import math
print(f"it's math! It has type {math}")
print(dir(math))

print("pi t 4 significant digits={:.3}.".format(math.pi))


# Printing the log of 
print(math.log(8,8))

import math as mt # this means renaming of the module name for your own reference of code
# here: math as mt means assume math as a mt and later on take that mt to print.
print(mt.pi)

# Importing the Specific item
# Instead of importing the entire module, just import the specific function or variable we need. like this one
from math import pi, log
print(pi)
print(log(12,8))

# importing all as one
# from math import*
# from numpy import*
# this may cause conflict while coding as both libraries may contain same name of function


# here it imports a numpy and while printing it takes submodule as numpy.random.randint(1,1)
import numpy
print(numpy.random.randint(1,14))
arr=numpy.array([1,2,3,4,5,6,7,8])
print(type(arr))
mean=arr+2
print(mean)
# this means that that mean will skip those +2 value and will count like 3,4,5,6,7,8,9,10 just 

# print(dir(arr))
# help(arr)
# this will 

ab='amit is mutthal'
print(numpy.asarray(ab))