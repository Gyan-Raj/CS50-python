def meow(n: int) -> str:
    return f"meow\n" * n


number: int = int(input("Enter a number: "))
meows: str = meow(number)
print(meows, end="")


r"""
run "mypy 02_type_hints.py" to see this output:
PS C:\Users\bhard\Desktop\learning\CS50-python\14-et cetera\06_type_hints> mypy .\02_type_hints.py
Success: no issues found in 1 source file
"""
