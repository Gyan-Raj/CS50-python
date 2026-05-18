# Tuples are immutable
def main():
    user = get_user()
    if user[0].lower() == "gyan":
        user[1] = "Raj"
    print(f"Hi, {user[0]} {user[1]}")


def get_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    # return first_name, last_name will also return a tuple, but to be explicit, we do return (first_name, last_name)
    # return first_name, last_name
    return (first_name, last_name)


if __name__ == "__main__":
    main()

r"""
# When we try to run this script by entering first name as "gyan" and second as <anything>, then we will get error (TypeError) because because tuples are immutable
Traceback (most recent call last):
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\01-tuple\02_tuple.py", line 18, in <module>
    main()
    ~~~~^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\01-tuple\02_tuple.py", line 5, in main
    user[1] = "Raj"
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""


"""
SO, we can use "list" if we want to mutate the values (like in 01_tuple.py), but a better way would be a dictionary (dict)
03_dict.py
"""