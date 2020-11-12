def print_msg(msg):
    def printer():
        print(msg)

    printer()


def print_msg2(msg):
    def printer():
        print(msg)

    return printer


print_msg("Hello")

#closure
another = print_msg2("Hello")
another()