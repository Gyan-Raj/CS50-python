# Why not move the get_user method inside User class itself, so that we can have all business related to user at one place - inside its class

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Object created for {self.first_name} {self.last_name}"

    @classmethod
    def get(cls):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        return cls(first_name, last_name)


def main():
    user = User.get()
    print(f"Hello {user.first_name} {user.last_name}")


if __name__ == "__main__":
    main()
