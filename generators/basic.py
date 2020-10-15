list = [1,2,3,4]

def test(list):
    for i in list:
        yield i


t = test(list)

print(next(t))
print(next(t))
print(next(t))
print(next(t))
