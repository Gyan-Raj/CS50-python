from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 9
    assert square(-3) == 9
    assert square(0) == 0


if __name__ == "__main__":
    main()


"""
Now, to use "pytest":
  - run the file by "pytest test_calculator.py"
  - we will now see the error as:
        collected 1 item                                                                                                                            

        test_calculator.py F                                                                                                                  [100%]

        ================================================================= FAILURES =================================================================
        _______________________________________________________________ test_square ________________________________________________________________

            def test_square():
                assert square(2) == 4
        >       assert square(3) == 9
        E       assert 6 == 9
        E        +  where 6 = square(3)

        test_calculator.py:10: AssertionError
        ========================================================= short test summary info ==========================================================
        FAILED test_calculator.py::test_square - assert 6 == 9
        ============================================================ 1 failed in 0.21s =============================================================
"""
# The error above is self explanatory
