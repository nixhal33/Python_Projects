# '\' ----> sign can help to escape out from 's sign
# like here i put nix's time but there's already ' sign there so when compiling the output will be error so please use this '\' sign to avoid error.
# this is simply taking the strings assigned to the value like message ,1 or 2
message = 'Hello world bitch!'
message1 = 'This is nix\'s time '
message2 = """This is nix time and i am the king of this world""" # this """ """ sign is valid in python..
# this is simply printing message 
print(message)
print(message1+message2)
print(len(message+message1+message2))
# this message[3] or message[0:3] or message[:3] or message[6:9] is an index for that string value.
# for eg: message[0:3] means the message variable that contains the message strings as message='Hello world bitch!' here this the index[0:3] means it will print Hell cuz index always starts from 0 put will not print the last word like 0:4 it will take 0 but not print 4 like in Hello it will take Hel only but not O and i currently dunno about this.
print(message[3]+message1[5]+message2[8])
print("this one")
print(message[0:4]+message1[5:]+message2[:8])
# Prints the message2 strings as a upper and lower case
print(message2.lower())
print(message1.upper())

      
