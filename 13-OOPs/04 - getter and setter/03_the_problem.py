"""
In 01_getter_setter.py, we learnt that if we use getter-setter and then try to change the values of object (animal.animal_name = "rat"), it thre error
And, so in 02_getter_setter.py we used a better approach of it, where we had validations of setter at one place
NOTE that we cannot now override last_name as: user.last_name = "rAj" as it will throw error (ValueError: Incorrect last name)
BUT BUT BUT, we can still override it as: user._last_name = "rAj"
So, what is use of getter and setter?
"""
# The following code is same as 02_getter_setter, just that instead of user.last_name = "rAj", which was throwing ValueError (ValueError: Incorrect last name), we are now using user._last_name = "rAj", which no longer throws any error


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
    user._last_name = "rAj"
    print(f"Hello {user.first_name} {user.last_name}")


def get_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return User(first_name, last_name)


if __name__ == "__main__":
    main()

r"""
This will no longer throw any ValueError (ValueError: Incorrect last name):
- Pyhton does not have any concept of private or publuc functions/variables.
- Developers use "_" to show that other developers should not touch the variables using "_" directly. However, they are able to do it, they should not
- We can also use double undersores "__" for such varables as well
"""
# So, it is just the coding standard that we should follow
