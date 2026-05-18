# Compared to 04_class, the following is a better way to create class
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def main():
    user = get_user()
    if user.first_name.lower() == "gyan":
        user.last_name = "Raj"
    print(f"Hi, {user.first_name} {user.last_name}")


def get_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user = User(first_name, last_name)
    return user


if __name__ == "__main__":
    main()
