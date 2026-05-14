from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()


# AssertionError
"""
The code will throw error something like this:
Traceback (most recent call last):
  File "C:\Users\bhard\Desktop\learning\CS50-python\10-unit testing\02-assert\test_calculator.py", line 14, in <module>
    main()
    ~~~~^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\10-unit testing\02-assert\test_calculator.py", line 5, in main
    test_square()
    ~~~~~~~~~~~^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\10-unit testing\02-assert\test_calculator.py", line 10, in test_square
    assert square(3) == 9
           ^^^^^^^^^^^^^^
AssertionError
"""

# The error above is not readable, so we need to handle the AssertionError in try-except block (03-assert-in-try-except)