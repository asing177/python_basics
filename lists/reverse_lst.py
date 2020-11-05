numbers = [1,2,3,4,5]


def method1(lst):
    if len(lst) == 1:
        return lst
    return method1(lst[1:]) + lst[0:1]



print(method1(numbers))


def method2(lst):
    for i in range(int(len(lst)/2)):
        temp = lst[i]
        lst[i] = lst[len(lst)-i-1]
        lst[len(lst)-i-1] = temp

    return lst


print(method2(numbers))