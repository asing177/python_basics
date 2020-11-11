ele = "alpha"

with open("file.txt") as f:
    res = f.readlines()
    res = [i.split() for i in res]


def check_pos(str, arr):
    count = 0
    data = []

    for i in arr:
            for pos,j in enumerate(i):
                count = count + 1
                if j == str:
                    data.append(count)
    return data


print(check_pos(ele, res))