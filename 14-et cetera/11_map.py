def main():
    yell("Learning", "Pyhton", "from", "CS50")


def yell(*words):
    print("Named arguments:", words)
    print("Type of named arguments:", type(words))
    # map takes two arguments: 1. the function that has to be run on each element of tuple and 2. The tuple
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
