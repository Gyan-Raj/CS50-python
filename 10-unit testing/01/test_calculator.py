from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared is not 4")
    if square(3) != 9:
        print("3 squared is not 9")


if __name__ == "__main__":
    main()

# NOTE: There is a lot of line of code just to test a square function, moreover, we have just covered 2 test cases (for 2 and 3)
# So, we will be using "assert" - 02-assert