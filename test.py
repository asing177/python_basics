import time
import math

def decorate(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner

@decorate
def factorial(num):
    time.sleep(2)
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i


factorial(10)