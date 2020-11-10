class Descriptor(object):

    def __init__(self, name=''):
        self.name = name

    def __get__(self, obj, objtype):
        return "{} from class".format(self.name)

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")


class Test(object):
    name = Descriptor()


t = Test()
t.name = "hello"
print(t.name)