# We can not do validation in setter functions directly - skipping validations in __init__

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name:
            raise ValueError("First name cannot be empty")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name not in ["raj", "Raj"]:
            raise ValueError("Incorrect last name")
        self._last_name = last_name


def main():
    user = get_user()
    user.last_name = "rAj"
    print(f"Hello {user.first_name} {user.last_name}")


def get_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return User(first_name, last_name)


if __name__ == "__main__":
    main()

"""
This will throw error:
Traceback (most recent call last):
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\04 - getter and setter\02_getter_setter.py", line 42, in <module>
    main()
    ~~~~^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\04 - getter and setter\02_getter_setter.py", line 31, in main
    user.last_name = "rAj"
    ^^^^^^^^^^^^^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\04 - getter and setter\02_getter_setter.py", line 25, in last_name
    raise ValueError("Incorrect last name")
ValueError: Incorrect last name
"""