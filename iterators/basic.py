class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1


a, b = 2, 5

c1 = Counter(a, b)
c2 = Counter(a, b)

for i in c1:
    print(i)


it = iter(c2)
try:
    while True:
        print(next(c2))
except:
    print("Iteration Over")
