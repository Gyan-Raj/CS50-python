"""
__str__ method has access to the current object
- so instead of "Hello user object", we do also have acess of the first_name and last_name passed while creation of this object
- f"Object for {self.first_name} {self.last_name} is created"
"""


class User:
    def __init__(self, first_name, last_name):
        if not first_name:
            raise ValueError("first_name cannot be empty")
        if last_name not in ["Raj", "raj"]:
            raise ValueError("Last name is incorrect")
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Object for {self.first_name} {self.last_name} is created"


def main():
    user = get_user()
    print(user)  # Hello user object
    if user.first_name.lower() == "gyan":
        user.last_name = "Raj"
    print(f"Hi, {user.first_name} {user.last_name}")


def get_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return User(first_name, last_name)


if __name__ == "__main__":
    main()
