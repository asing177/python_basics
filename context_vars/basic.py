import contextvars

#Creating Context Var
cvar = contextvars.ContextVar("cvar", default="variable")

print("value:", cvar.get())


# calling set method
token = cvar.set("changed")

print(token.var)


print("value:", cvar.get())

# checking the type of token instance
print("Type:", type(token))

print(token.old_value)

token = cvar.set("changed_2")
print("Value:", token.old_value)

cvar.reset(token)

print("Value:", cvar.get())