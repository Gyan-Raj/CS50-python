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
    print(f"{animal.name}: {animal.emoji()}")


def get_animal():
    animal_name = input("Enter animal name: ")
    return Animal(animal_name)


if __name__ == "__main__":
    main()
