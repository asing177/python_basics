str = "hello"


def check_freq(str):
    all_freq = {}

    for i in str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    res = min(all_freq, key=all_freq.get)

    return res




print(check_freq(str))