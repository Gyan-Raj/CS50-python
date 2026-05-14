from greet import hello, goodbye


def test_hello_default():
    assert hello() == "Hello, World"


def test_goodbye_default():
    assert goodbye() == "Goodbye, World"


def test_hello_argument():
    assert hello("Gyan") == "Hello, Gyan"


def test_goodbye_argument():
    assert goodbye("raj") == "Goodbye, raj"
