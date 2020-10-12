str = "aaacodedoc"

def palindromeCutting(str):
    prefix = get_palindrome_prefix(str)
    print(prefix)



def get_palindrome_prefix(str):
    prefix = str[0]+str[1]+str[2]+str[3]
    if prefix == prefix[::-1]:
        return prefix
    else:
        pass



palindromeCutting(str)