# Call by Object Reference

string = "abcd"


def test(string):
    string = "1234"
    print("Inside :", string)


test(string)
print("Outside :", string)


def add(list):
    list.append(50)
    print("Inside : ", list)


mylist = [10, 20, 30, 40]

add(mylist)
print("Outside :", mylist)



a = [1,2,3]
def foo(b):
	b.append(4)
	c = b[:]
	c.append(11)
	return c

c = foo(a)
print(a,c)

