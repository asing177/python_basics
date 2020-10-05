# Call by Object Reference

string = "abcd"


def test(string):
    string = "1234"
    print("Inside :", string)


test(string)
print("Outside :", string