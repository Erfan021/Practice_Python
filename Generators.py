# !-- GENERATORS --!

def generator_functiom(num):
    for i in range(num):
        yield i * 4
        

g = generator_functiom(100)
next(g)
next(g)
print(next(g))

for item in generator_functiom(100):
    print(item)
    
#def make_list(num):
#    result = []
#    for i in range(num):
#        result.append(i*4)
#        
#    return result
#
#
#my_list = make_list(100)
#print(my_list)

from time import time
def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took : {t2-t1} s')
        return result
    return wrap_func


@performance
def long_func():
    print('1st')
    for i in range(100000000):
        i * 2
        

@performance
def long_func2():
    print('2nd')
    for i in list(range(100000000)):
        i * 2
        

long_func()
long_func2()

def for_backend(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break
        

for_backend([1,2,3,4,5,6])

# Fibonacci Numbers:-

def fib(num): # Generator
    a, b = 0, 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
        
        
for x in fib(21):
    print(x)
        

def fib_list(num): # List
    a, b = 0, 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result
        
        
print(fib_list(21))



