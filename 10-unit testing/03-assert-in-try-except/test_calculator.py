from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")


if __name__ == "__main__":
    main()


# This is fine, but again we have reached to the first case where we were writing test in "if" statements. So, this will also again have too many lines of codes for multiple edge case testing

"""
So, we use "pytest" library for testing (04-pytest) where we need to:
  - install pytest : pip install pytest
  - run the file by "pytest file_name.py"
"""
