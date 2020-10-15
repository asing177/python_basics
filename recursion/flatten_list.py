l = [22 , 2, [1, 2, 3], 5, 6, [4, [5, 6]], [7], [8, 9] , 10 , 11]


def flatten(l):
    flat_list = []
    for sublist in l:
        if isinstance(sublist, list):
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)

    return flat_list


print(flatten(l))