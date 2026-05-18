def main():
    user = get_user()
    if user["first_name"].lower() == "gyan":
        user["last_name"] = "Raj"
    print(f"Hi, {user["first_name"]} {user["last_name"]}")


def get_user():
    user = {}
    user["first_name"] = input("Enter your first name: ")
    user["last_name"] = input("Enter your last name: ")
    return user


if __name__ == "__main__":
    main()

"""
Instead of these dictionaries, we can also create a "class" which is a better way of creating objects 04_class.py 
"""