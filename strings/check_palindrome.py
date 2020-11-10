str = "malayalam"


def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

def check_palindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True



print(isPalindrome(str))
print(check_palindrome(str))


