nums={'one':1 ,'two':2 ,'three':3 , 'eleven':11}
print(nums['one'])
print('eleven')

planet={'Mercury': 'M',
 'Venus': 'V',
 'Earth': 'E',
 'Mars': 'M',
 'Jupiter': 'J',
 'Saturn': 'S',
 'Uranus': 'U',
 'Neptune': 'N'
}
print('Neptune' in planet)
print('Pluto' in planet)
for k in planet:
    print("{} = {}".format(k+ ', Hello', planet[k]))

'''Keys: "Mercury", "Venus", "Earth", etc.
Values: "M", "V", "E", etc.'''

for planet, i in planet.items():
    print(f"{planet} begins with {i}.")

# for value in planet.values():
#     print(f"Temp var is {value}")

friend={
    'naren':'a',
    'amit' : 'b',
    'bubu' : 'c',
}
for friend, value in friend.items():
    print(f"{friend} is equal to {value}")


#########new dictionary################

recipie=('Food','Drink','liquor','Dessert')
combo=('Butter Chicken','Xtreme Energy Drink','Jack Danials 9000','Red Magnum Ice Cream')
zipping=dict(zip(recipie,combo))
print(zipping)
# this will make a dictionary out of these two tupples by combining them together as you can see the output.