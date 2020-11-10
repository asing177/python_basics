import time
import random
def random_num(x):
    random = int(time.time()*1000)
    random %= x
    return random


print(random.randint(1,100))
print(random_num(100))