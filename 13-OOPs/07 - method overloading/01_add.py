"""
wherever we use "+" between two entities, it calls the "__add__" method.
We can override that method as:
"""


class Marks:
    def __init__(self, physics=0, chemistry=0, maths=0):
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def __str__(self):
        return (
            f"Physics: {self.physics}, Chemistry: {self.chemistry}, Maths: {self.maths}")

    def __add__(self, other):
        physics = self.physics + other.physics
        chemistry = self.chemistry + other.chemistry
        maths = self.physics + other.maths
        return Marks(physics, chemistry, maths)


User1 = Marks(80, 83, 90)
User2 = Marks(70, 77, 95)
total = User1 + User2
print(total)
