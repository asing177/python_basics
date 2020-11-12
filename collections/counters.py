from collections import Counter

print(Counter(['B','B','A','B','C','A','B','B','A','C']))
print(Counter({'A':3, 'B':5, 'C':2}))
print(Counter(A=3, B=5, C=2))



c = Counter()
c.update([1, 2, 3, 1, 2, 1, 1, 2])
print(c)
c.update([1, 2, 3, 1, 2, 1, 1, 2])
print(c)

c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)

c1.subtract(c2)
print(c1)
