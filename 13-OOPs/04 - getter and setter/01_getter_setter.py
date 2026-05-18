"""
# The below code is same as 02_custom_methods.py, just that here we overide the animal object by doing
animal.name = "human" in the main method and we can see that even if we enter "cow" as animal name, it will still show "human: 🧑" in the output
To avoid this, we use "property", "decorators", "setter etc (04 - getter and setter) 
"""


class Animal:
    def __init__(self, name):
        if not name:
            raise ValueError("Animal name cannot be empty")
        self.animal_name = name

    def __str__(self):
        return f"Created {self.animal_name} object"

    def emoji(self):   # every function/method inside class must have atleast one parameter (which is "self" (can be named anything)) which will represent that object itself
        match self.animal_name:
            case "cow" | "Cow":
                return "🐂"
            case "human" | "Human":
                return "🧑"

    @property
    def animal_name(self):
        # We use _animal_name and not animal_name because in __init__ we already have a variable named "animal_name" (self.animal_name = name)
        # We cannot have a variable as well as a function with same name (animal_name) as, it will collide and python will not allow this.
        # So, to differentiate, we use this kind of convention
        return self._animal_name

    @animal_name.setter
    def animal_name(self, name):
        if name not in ["cow", "Cow", "human", "Human"]:
            raise ValueError("Invalid animal")
        # We use _animal_name and not animal_name because in __init__ we already have a variable named "animal_name" (self.animal_name = name)
        # We cannot have a variable as well as a function with same name (animal_name) as, it will collide and python will not allow this.
        # So, to differentiate, we use this kind of convention
        self._animal_name = name


def main():
    animal = get_animal()
    animal.animal_name = "rat"
    print(f"{animal.animal_name}: {animal.emoji()}")


def get_animal():
    name = input("Enter animal name: ")
    return Animal(name)


if __name__ == "__main__":
    main()

r"""
PS C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\04 - getter and setter> python .\01_getter_setter.py
Enter animal name: cow
Traceback (most recent call last):
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\04 - getter and setter\01_getter_setter.py", line 53, in <module>
    main()
    ~~~~^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\04 - getter and setter\01_getter_setter.py", line 43, in main
    animal.animal_name = "rat"
    ^^^^^^^^^^^^^^^^^^
  File "C:\Users\bhard\Desktop\learning\CS50-python\13-OOPs\04 - getter and setter\01_getter_setter.py", line 34, in animal_name
    raise ValueError("Invalid animal")
ValueError: Invalid animal
"""
# Although we give animal name as "cow", it raises exception "ValueError: Invalid animal" because we are trying to assign name as "rat" (animal.animal_name = "rat") which does not belong to the list mentioned in setter method (if name not in ["cow", "Cow", "human", "Human"]:)
