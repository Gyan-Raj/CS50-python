from calculator import square, cube


def test_square_positive():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9


def test_square_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9


def test_square_zero():
    assert square(0) == 0


def test_cube_positive():
    assert cube(1) == 1
    assert cube(2) == 8
    assert cube(3) == 27


def test_cube_negative():
    assert cube(-1) == -1
    assert cube(-2) == -8
    assert cube(-3) == -27


def test_cube_zero():
    assert cube(0) == 0
