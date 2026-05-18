"""
The methods that we saw earlier in a class (__init__, __str__, emoji, animal_name, first_name, last_name etc) are called instance methods
What we are going to see now is classmethod
"""

import random


class User:
    last_name = ["raj", "Raj",  "rAj", "raJ", "RAj", "rAJ", "RaJ", "RAJ"]

    @classmethod
    def full_name(cls, first_name):
        print(f"Hi {first_name} {random.choice(cls.last_name)}")


User.full_name("gyan")
