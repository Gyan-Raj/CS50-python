# We are forcing user to give a +ve number, else it will keep asking user for a positive value infinetly
while True:
    n = int(input("Enter a positive number: "))
    if n > 0:
        break

for _ in range(n):
    print("Hi")


# OR
def main():
    num = get_number()
    print_hi(num)


def get_number():
    while True:
        n = int(input("Enter a positive number: "))
        if n > 0:
            break
    return n


def print_hi(n):
    for _ in range(n):
        print("Hi")


main()
