# list is a datatype in python (str, int, bool, float, list)
for i in [0, 1, 2]:
    print("Hi", i)


# The problem with code above is: what if we have to print "Hi" 500 times
for i in range(3):
    print("Hi", i)  # NOTE: i starts from 0 and goes upto 2 (excluding 3)


# if we don't have any usage of i, we can use "_" like:
for _ in range(3):
    print("Hi")

# However, if we try to print "_", it will give us 0,1,2 (as it is just for symbolizing that although we are iterating but we are not going to use the index, so we use "_")
for _ in range(3):
    print("Hi", _)


# printing can also be done as:
print("Hi\n" * 3)  # but this will give another empty line at the end (because the default value of end is "\n", so we need to override it as)
print("Hi\n" * 3, end="")
