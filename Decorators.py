# !--DECORATORS--!

def hello(func):
    func()
    
def greet():
    print('hey everyone')
    
hi = hello(greet)
print(hi)

def my_decorator(func): #decorator pattern
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs) 
    return wrap_func


@my_decorator
def hello(greet, emoji=':)'):
    print(greet, emoji)
    

hello('hi everyone')


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
    for i in range(100000000):
        i * 2
        

long_func()


































