# program for anagram strings
# An anagram of a string is another string that contains same characters,
# only the order of characters can be different.


def anagram(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    # Compare lengths of both strings
    # If length not equal then false
    if n1 != n2:
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return False

    return True


str1 = "test"
str2 = "ttee"
print(anagram(str1, str2))
