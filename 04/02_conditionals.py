num = int(input("Enter the number: "))
if (num % 2 == 0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# another way to write code:
def main():
    x = int(input("Enter the number: "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")


# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# # is_even can also be defined as:
# def is_even(x):
#     return True if x % 2 == 0 else False


# # is_even can further be rewritten as:
def is_even(x):
    return x % 2 == 0

main()
