# Get the longest palindrome prefixes
# if the prefix has 2 or more chars then cut the longest prefix from string
# else return the original string

str = "codesignal"
str1 = "aaacodecdoc"

def palindromeCutting(str):
    prefix = longest_palindrome(str)
    if len(prefix) >= 2:
        new_string = remove_prefix(str, prefix)
    else:
        new_string = str

    return new_string


def remove_prefix(str, prefix):
    if str.startswith(prefix):
        return str[len(prefix):]
    return str

def longest_palindrome(str):
    max = 0
    for length in range(0,len(str)):
        prefix = str[0:length]
        temp = prefix
        temp2 = temp[::-1]
        if temp == temp2:
             max = length
             palidrome = prefix

    return palidrome



print(palindromeCutting(str))