"""
# The below code is same as 02_custom_methods.py, just that here we overide the animal object by doing
animal.name = "human" in the main method and we can see that even if we enter "cow" as animal name, it will still show "human: 🧑" in the output
To avoid this, we use "property", "decorators", "setter etc (04 - getter and setter) 
"""


class Animal:
    def __init__(self, name):
        if not name:
            raise ValueError("Animal name cannot be empty")
        self.name = name

    def __str__(self):
        return f"Created {self.name} object"

    def emoji(self):   # every function/method inside class must have atleast one parameter (which is "self" (can be named anything)) which will represent that object itself
        match self.name:
            case "cow" | "Cow":
                return "🐂"
            case "human" | "Human":
                return "🧑"
            case _:
                return "🦠"


def main():
    animal = get_animal()
    animal.name = "human"
    print(f"{animal.name}: {animal.emoji()}")


def get_animal():
    animal_name = input("Enter animal name: ")
    return Animal(animal_name)


if __name__ == "__main__":
    main()
