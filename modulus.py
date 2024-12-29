def mod_5(x):
    return x % 5

print(
    'What is the biggest is the biggest?', max(100,500,35),
    'what is the biggest modulo using 5' , max(100,400,35 ,key=mod_5),
    sep='\n'

)