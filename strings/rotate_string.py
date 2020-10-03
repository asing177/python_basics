# Given a string of size n, write functions to perform following operations on string.
# Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
# Right (Or clockwise) rotate the given string by d elements (where d <= n).

# Input : s = "qwertyu"
# d = 2
# Output :
# Left rotation : "ertyuqw"
# Right rotation : "yuqwert"


def rotate(input, d):
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    # now concatenate two parts together
    print("Left Rotation : ", (Lsecond + Lfirst))
    print("Right Rotation : ", (Rsecond + Rfirst))



input = 'GeeksforGeeks'
d=2
rotate(input,d)