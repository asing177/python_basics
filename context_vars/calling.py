import contextvars

user_id = contextvars.ContextVar("user_id")

def f1(user, operation):
    user_id.set(user.id)
    f2()

def f2():
    f3()

def f3():
    print(user_id.get(default=None))


f3()