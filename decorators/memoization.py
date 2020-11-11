def memoize_factorial(f):
    memory = {}

    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))