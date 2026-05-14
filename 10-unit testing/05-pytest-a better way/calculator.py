def main():
    num = int(input("Enter the number: "))
    print(f"Square of {num} is {square(num)}")
    print(f"Cube of {num} is {cube(num)}")


def square(n):
    return n * n


def cube(n):
    return n * n * n


if __name__ == "__main__":
    main()
