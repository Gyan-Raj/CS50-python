def main():
    user = get_user()
    if user[0].lower() == "gyan":
        user[1] = "Raj"
    print(f"Hi, {user[0]} {user[1]}")


def get_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    # We are returning list and then mutating its value at line 4 (if first name is entered as "Gyan")  =>  This is OK
    # But, if we return a "tuple", it will throw error (Since, tuple is immutable)  =>  see 02_tuple.py
    return [first_name, last_name]


if __name__ == "__main__":
    main()
