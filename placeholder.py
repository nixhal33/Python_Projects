greet='Hello'
name='Nix'
# concatenation means combining two or more strings into one or two or more variables into one
# using literals for space and commas and also don't forget to use before and after using the '' literal sign.
# this is a simple one but not so convienent while doing projects.
new_message = greet+', '+ name + '. Welcome!'
print(new_message)

# best format method to use is this 
print('************This is the best way**********')
# this '{}, {}. Welcome!' .format(name,greet) means {} means placeholder for two variables  and .format(name,greet) means while printing the format the name comes forward first and and greet after then.
new_message = '{}, {}. Welcome!' .format(name,greet)
print(new_message)

