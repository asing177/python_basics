arr = []

length = int(input())

for i in range(length):
    elem = input()
    arr.append(elem)

def concatEdgeLetters(arr):
    combo_list = []

    first, last = arr[0], arr[-1]

    for index, word in enumerate(arr):
        try:
            chars = get_chars(word)
            adjacent_chars = get_chars(arr[index+1])
            combos = create_combos(chars,adjacent_chars)
            combo_list.append(combos)
        except:
            pass

    final_chars = final_combo(get_chars(first), get_chars(last))
    combo_list.append(final_chars)
    print(combo_list)


def get_chars(word):
    return (word[0],word[-1])


def create_combos(chars,adjacent_chars):
    return chars[0]+adjacent_chars[-1]


def final_combo(chars, adjacent_chars):
    return adjacent_chars[0]+chars[-1]




concatEdgeLetters(arr)