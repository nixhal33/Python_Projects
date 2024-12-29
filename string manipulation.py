print('what\'s up?')
print("hello \nworld")
print('You \'ve got a \"cool\" bike!')
print('look, a mountain /\\')

triplequoteuse="""Roman Reign
Undertaker
Stone Cold
Cody Rhoades
Lana Rhoades
Triple H
"""
print(triplequoteuse)
# here """ can be used to print whatever way you want as you wish for eg:
triplequoteuse1="""Mero ghar biratnagar ma xa ra ma nepal ma baas garxu mero baba india ma kaam garnu hunxa ra ma bau ko paisa ma moj masti gari raxu kamaune bela vaisakyo khai kaile bau ama lai sukha dine ho maile gedai jasto jindagi vaisakyo mero ta"""
print(triplequoteuse1)

# print("hello", end='')
# print("world", end='')

name='Amit is a good boy'
print(len(name[-3:]))
new_name=[
    i for i in name
]
print(new_name)
print("name for index is", name.index('m'))
print(name.startswith('a')) # checks if name='Amit' starts with a
print(name.endswith('t')) # checks if Amit ends with t 
print(name.split()) # since name got those long words we can split those strings into different one or smaller strings 

###########################
nickname='Amit and naren are best friends'
print(nickname.upper())
nickname.upper() # this will not execute cuz it does not have print function

words = ['pluto', 'is', 'a', 'planet']
result=' 👏 '.join([word.upper() for word in words])
print(result)

# another one ".join" are keywords 
mess="Amit is a very bad boy"
print(mess)
new_mess=" ❤️ ".join([temp.upper() for temp in mess])
print(new_mess)

# use of str() fnc and is used when we need to throw any non string object
data=[1,2,3,4,5] # as you can see this is a numeric data
reslt=', '.join([str(x) for x in data]) # we can see that str() is used to explicitly convert the numeric data into string form 
print(reslt)
# -------------------------
planet='Pluto'
position=9
print(planet+", you will always be in "+str(position)+"th postition to me.")

# for more easier configuration or easier format
# use of format
print("{}, you 'll always be {}th position planet for me.".format(planet,position))

# much easier form to use the format 
print(f"{planet} you will always be in {position}th planet for me.")

# value taken from the planet
pluto_mass=1.303 * (10**2)
earth_mass=5.9722 * (10**24)
popln=5210390 
print("{} weighs about {:} kilograms ({:} of Earth's mass).It is the home to plutonains.The population is around {:,} on the Pluto".format(planet,pluto_mass,pluto_mass / earth_mass, popln))
# here this {:.3} {:.2} means fixing upto 2 or 3


# in format you don't need to create a random list 
s="""Earth's a {0} planet no! earth's a {1}!
{0}!
{1}!
Jupiter is the {2} in the worlDictionary!
 """.format('largest','3rd largest','Bigass planet')
print(s) 
