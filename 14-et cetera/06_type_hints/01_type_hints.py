# Similar to javascript, python is dynamically types language
# We can however use a tool "typing" provided in "mypy" package (pip install mypy) which can do type checking for us. This will not break the code but will just highlight the type mismatches before releasing the code
# Run this file using "mypy 01_type_hints.py" beofre running "python 01_type_hints.py"

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Enter a number: "))
meow(number)

r"""
When we run "mypy 01_type_hints.py", it will show this output:
C:\Users\bhard\Desktop\learning\CS50-python\14-et cetera\06_type_hints> mypy .\01_type_hints.py
Success: no issues found in 1 source file
"""

# NOTE: the default return type of a function is "None"
