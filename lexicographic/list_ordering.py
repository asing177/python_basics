l1=['a', 'b' , 'c' , 'd']
l2=['abc' , 'cd' , 'xy' , 'ba' , 'dc']

result = ['abc' , 'cd']

l2.sort()
print(l2)


def func(l1,l2):
    result = []
    for i in l2:
        for j in l1:
            if j in i:
                result.append(i)
    
    result = list(set(result))
    result.sort()
    return 

func(l1,l2)