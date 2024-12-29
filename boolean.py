# x = True
# print(x)
# print(type(x))

# finding the boolean using the function
def are_you_adult(age):
    """Are you the one riding bike,Are you adult?"""
    return age>=18

print("Are you adult to ride bicycle at 43 ?", are_you_adult(43))
print("Are you adult to ride bicycle at 10 ?", are_you_adult(10))

# if citizen can become president whose age is greater than 45
def run_for_president(age, is_citizen):
    return  is_citizen and (age >=45)

run_for_president(17, True)
run_for_president(45, False)
run_for_president(45, True)
