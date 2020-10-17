import json

def decorate(func):
    def inner(*args , **kwargs):

        return json.dumps(func(*args, **kwargs))

    return inner

@decorate
def return_dict(a,b):
    return {'x':a,'y':b}


print(return_dict(1,2))