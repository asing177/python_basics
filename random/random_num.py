import time

def random_num(x):
    random = int(time.time()*1000)
    random %= x
    return random

print(random_num(100))