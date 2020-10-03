l1 = [5, 1 , 3 , 4, 10 ,16, 19 , 0]

min =  l1[0]
min2 = l1[1]

for i in l1:
    if i < min:
        min2 = min
        min = i
    elif (i < min2 and i != min): 
        min2 = i

print(min)
print(min2)
