def main():
    num = int(input("Enter the number: "))
    print(f"Square of {num} is {square(num)}")


def square(n):
    return n + n      # Intentianally doing n+n instead of n*n, so that we can seee how error is seen while testing


if __name__ == "__main__":
    main()
