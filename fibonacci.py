#     Fibonacci numbers is defined by the recurrence relation
#     Fn = Fn-1 + Fn-2
#     F0 = 0 and F1 = 1.

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(9))