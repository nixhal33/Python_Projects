def is_odd(x):
    return (x % 2) ==1

print('Is 100 odd ?', is_odd(100))
print('Is -69 odd ?' , is_odd(-69))

# new one for the actual boolean check
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(35, False))
print(can_run_for_president(55, True))

