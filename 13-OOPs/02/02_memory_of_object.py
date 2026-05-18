class User:
    def __init__(self, first_name, last_name):
        if not first_name:
            raise ValueError("first_name cannot be empty")
        if last_name not in ["Raj", "raj"]:
            raise ValueError("Last name is incorrect")
        self.first_name = first_name
        self.last_name = last_name


def main():
    user = get_user()
    print(user)  # <__main__.User object at 0x0000024B998486E0>
    # 0x0000024B998486E0 shows the address of the object created in memory (This will change everytime we run the script)
    # To override this behaviour, pyhton exposes another method "__str__" (02_(__str__).py)
    if user.first_name.lower() == "gyan":
        user.last_name = "Raj"
    print(f"Hi, {user.first_name} {user.last_name}")


def get_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return User(first_name, last_name)


if __name__ == "__main__":
    main()
