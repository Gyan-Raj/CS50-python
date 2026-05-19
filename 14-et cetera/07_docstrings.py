# This again is a third party library used to create documentation of the code
# It detects comments written inside triple quotes
def meow(n: int) -> str:
    """
    Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Enter a number: "))
meows: str = meow(number)
print(meows, end="")
