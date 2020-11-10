str = "hello"


def check_freq(str):
    count = 0

    for i in str:
        current_freq = str.count(i)
        if current_freq > count:
            count = current_freq
            chr = i

    return chr


print(check_freq(str))