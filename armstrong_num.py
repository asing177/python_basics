# Given a number x, determine whether the given number is Armstrong number or not.
# A positive integer of n digits is called an Armstrong number of order n
# (order is number of digits) if
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
# 153
# 1*1*1 + 5*5*5 + 3*3*3 = 153 is armstrong
# 120
# 1*1*1 + 2*2*2 + 0*0*0 = 9

def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)

    return x * power(x, y // 2) * power(x, y // 2)


# Calculate order
def order(x):
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10

    return n


def armstrong(x):
    n = order(x)
    temp = x
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

    return (sum1 == x)


x = 153
print(armstrong(x))

x = 1253
print(armstrong(x))