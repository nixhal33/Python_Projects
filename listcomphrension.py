# not a list comprehension
lst=[]
for i in range(0,8):
    lst.append(i)
print(lst)

# not a list comprehension
a=[1,2,3,4,5,6]
a2=[]
for i in a:
    a2.append(i**2)
print(a2)
sep='\n'

# another one not a list comprehension
cube=[]
for i in range(10):
    if i % 2 == 0:
        cube.append(i**3)
print('cubes:-',cube)

"""List comprehension
is actually that makes code more smaller or that will be executed on single or 2 line..
"""
square=[ x ** 2 for x in range(1,10) if x%2==0]
print(square)
# now this is real list comprehension





# now this is how we do the list comprehension
"""Code breakdown
1. first we create a list named minus that contain some no.
2. then we create a list comprehension on new variable called negative that will contain a new upcoming list of desired output
3. what we did in this negative list is that here this:
The part i-2 represents the operation or output you want to apply to each item in the list. This defines what will appear in the new list.
The for i in minus works like a loop in other programming languages (e.g., for loops in C++), where i is a temporary variable that iterates over each element in the list named minus.
Here, minus is a pre-existing list that contains valid data.
The if i % 2 == 0 acts as a condition. It filters the elements in minus, selecting only those that satisfy the condition (in this case, even numbers).
Finally, the new list negative will contain the results after applying the operation (i-2) to the filtered elements. You can then use print(negative) to display the output."
"""
minus=[1,2,3,43,4,5,66,4123,523]
negative=[i-2 for i in minus if i%2==0]
print(negative)

# another one
def count_negative(no):
    return sum([no < 0 for no in neg_no])
neg_no=[-5,1,-3,4,2,-4,-7]
result=count_negative(neg_no)
print(result)

# using the lambda function
pow_four=[1,2,3,4,5,6,7,8,9,10]
actual_pow_four=lambda num: [i**4 for i in num if i%2==0 ]
print(actual_pow_four(pow_four))

# another one using lambda function
no1=[1,2,3,4,5,6,7]
add=lambda x: x+2
print(add(5))
# here in this print we have to put the value that is inside of the list which we want as output


# # another one
# def count_negative(no):
#     return sum([no < 0 for no in neg_no])
# neg_no=[-5,1,-3,4,2,-4,-7]
# result=count_negative(neg_no)
# print(result)

def negativity():
    return sum(at < 0 for at in range(-5,10))
print(negativity())
#     range(-5, 10) generates numbers from -5 to 9.
#     The expression at < 0 checks whether each number (at) in this range is negative.
#     sum() counts how many times at < 0 is True (which is 1 for each match).

# So, it will sum up the True values (which are treated as 1), giving the total count of negative numbers in the range from -5 to 9.
