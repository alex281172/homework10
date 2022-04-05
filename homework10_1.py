
def simple_separator():
    print('*************')
result = simple_separator()
# -------------------------------------------
print('-' * 50)
def simple_separator():
    print('***********************')
simple_separator()


def simple_separator():
    print('*' * 10)
simple_separator()
# -------------------------------------------

print('-' * 50)
def long_separator(x):
    print('*' * x )

long_separator(3)
long_separator(4)
# -------------------------------------------
print('-' * 50)

def long_separator(simv, my_len):
    print(simv * my_len )

long_separator('-', 10)
long_separator('#', 5)
# -------------------------------------------
print('-' * 50)

def hello_world(simbol):
    long_separator('*', 10)
    print()
    print('Hello World' + simbol)
    print()
    long_separator('#', 10)
hello_world('!')

# -------------------------------------------
print('-' * 50)


def hello_who(who = 'World'):
    print(f'Hello {who}!')
hello_who()

def hello_who(who = 'World'):
    print(f'Hello {who}!')
hello_who('Max')

def hello_who(who = 'World'):
    print(f'Hello {who}!')
hello_who('Kate')

# -------------------------------------------
print('-' * 50)

def pow_many(power, *args):
    result = 0
    for counter in args:
        result += counter
    result = result ** power
    return result

print(pow_many(1, 1, 2) == 3)
print(pow_many(1, 2, 3) == 5)
print(pow_many(2, 1, 1) == 4)
print(pow_many(3, 2) == 8)
print(pow_many(2, 1, 2, 3, 4) == 100)
# -------------------------------------------
print('-' * 50)


def my_functions(**kwargs):
    for k, v in kwargs.items():
        print(k)
        print(v)


my_functions(name='Leo', age=10)
my_functions(name='Leo', age=10, is_man=True)
my_functions(name='Leo', is_man=True, age=10)
my_functions(name='Leo')
my_functions()
# -------------------------------------------
print('-' * 50)

print('-' * 50)
def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(k,'-->', v)


print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)
# -------------------------------------------
print('-' * 50)



def my_filter(iterable, function):
    result = []
    for counter in iterable:
        if function(counter):
            result.append(counter)
    return result
    # return list(filter(function,iterable))



print(my_filter([1, 2, 3, 4, 5], lambda x: x > 2) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True