# Similar to rest operator (...), we have it in python as well "*"
# *args is for positional arguments
# *kwargs is for named arguments


def f(*args, **kwargs):
    print("Positional argumets", args)
    print("Type of Positional argumets", type(args))  # tuple
    print("Named argumets", kwargs)
    print("Type of Named argumets", type(kwargs))  # dict


f(100, 200, 300, 400, [1, 2, 3, 4], phy=80, chem=83, maths=93)


"""
To understand this, the print statement must have been defined using the syntax above, which can be visualized as below:
def print(*objects, sep=" ", sep="\n", ...):
    for object in objects:
        ...

That is why we are able to access print statement in different formats as well:
print()
print("Hello")
print("Hello", "Gyan")
"""
