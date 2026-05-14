def main():
    name = int(input("Enter your name: "))
    print(hello(name))
    print(goodbye(name))


def hello(name="World"):
    return f"Hello, {name}"


def goodbye(name="World"):
    return f"Goodbye, {name}"


if __name__ == "__main__":
    main()
