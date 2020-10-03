test_str = "GeeksforGeeks"

print("The original string is : " + test_str)

# initializing K
K = 7

# Using join() + reversed()
# Reverse Slicing string
res = ''.join(reversed(test_str[0:K]))

# printing result
print("The reversed sliced string is : " + res)