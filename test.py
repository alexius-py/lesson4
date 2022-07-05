f = "*"*10

print(f)
def simple_separator():
    sep = "*"*10
    return sep

print (simple_separator())

def long_separator (count):
    sep = "*"*count
    return sep
print(long_separator(20))
print(long_separator(3) == '***') # True
print(long_separator(4) == '****') # True

def separator(simbol, count):
    sep = simbol*count
    return sep

print (separator('-', 10) == '----------') # True
print (separator('#', 5) == '#####') # True

def hello_world():
    print("   **********")
    print("Hello World!")
    print("   ##########")
    return
hello_world()

def hello_who(who="world"):
    print("**********")
    print('Hello '+ who + '!')
    print("##########")
    return

hello_who()
hello_who('Max')
hello_who('Kate')

def pow_many(power, *args):
    result = sum(args)**power
    return result

print(pow_many(1, 1, 2)) # == 3) # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3)) # == 5) # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1)) # == 4) # True -> (1 + 1)**2 == 4
print(pow_many(3, 2)) # == 8) # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4)) #  == 100) # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

def print_key_val (**kwargs):
    for k, v in kwargs.items():
        print(k, '-->', v)

print_key_val(name='Max', age=21)
print_key_val(animal ='Cat', is_animal=True)

def my_filter (iterable, function):
    result = list(filter(function, iterable))
    return result


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3)) # == [4, 5]) # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2)) # == [2]) # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3)) # == [1, 2, 4, 5]) # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba')) # == ['a', 'b']) # True


