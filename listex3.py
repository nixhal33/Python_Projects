hands=[
    ['j','k','l'], # don't forget to put , sign 
    ['m','n','o'],
]
print(hands)

planet=[
    'Mercury',
    'Jupiter',
    'Mars',
    'Venus',
    'Earth',
    'Pluto',
]
print(planet)

# to rename the required indexes
planet[2:4]='Vinland','Morox' # here it renamed the list from index 2 to 4
print(planet)
print('The no. of planet on this list is :-', len(planet))
print(sorted(planet))

num=[
    1,2,3,4,5,6,7,8,
]
print(sum(num))

a=100
print(a.imag)
c=a+3j
d=a+10j
print(c.imag)
print(d.imag)

x=37
print(x.bit_length())
print(x.bit_count())
print(max(4,8,9,66,9))


# trying to remove the list using the index no.
planet=['Mercury','Venus','Earth','Mars','Jupiter']
print(planet)
planets=['Saturn','Neptune','Pluto']
planet.extend(planets)
print(planet)
planet[0:2]=[]
print(planet)


