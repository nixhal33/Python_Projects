greet='Hello'
name='Nix'
# best format method to use is this 
print('************This is the best way**********')
# this '{}, {}. Welcome!' .format(name,greet) means {} means placeholder for two variables  and .format(name,greet) means while printing the format the name comes forward first and and greet after then.
new_message = f'{greet}, {name}. Welcome!'
print(new_message)