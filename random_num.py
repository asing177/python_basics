#python program for random number generation

import random

print(random.randint(0, 9))


#randomness with using random module
print(set(map(str,range(1,int(input())+1))).pop())