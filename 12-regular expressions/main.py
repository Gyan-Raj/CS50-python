"""
We have regex library (re) that comes in python by default
"""


"""
# Suppose we are asking user's name and are epecting it to be something like:
Gyan Raj
# BUT, user is in habit of writing it as:
Raj, Gyan
i.e., last name then a comma and then the first name
To handle this case, we can do:
last, first = name.split(", ")
name=f"{first} {last}"
# BUT, this again will break if there is no space after comma. We will see in the following example
"""


name = input("Enter your name: ").strip()
if "," in name:
    # If we enter name as "Raj,Gyan", it will give us ValueError (ValueError: not enough values to unpack (expected 2, got 1))
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"Hello {name}")

"""
# So, in above example we see that we are having issue for the whitespace which means that we need to cater for comma and an optional whitespace after it
# Unfortunetly, split does not support regular expressions to find matches to split the string. So, we have to use regex package for it
"""


import re
name = input("Enter your name: ").strip()

"""
re.search(pattern: str | Pattern[str], string: str, flags: _FlagsType = 0) -> (Match[bytes] | None):
    - It scans through string looking for a match to the pattern, returning a Match object, or None if no match was found.
"""
matches = re.search(r"^(.+), *(.+)$", name)
"""
(.+) will return the first match (last name) before the comma and then it will have a space and then the (.+) which will be the first name
"""
if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello {name}")

"""
We can write the logic in a more compact way by using "walrus operator" which allows us to assign a value to a variable as part of a larger expression, while also returning that value.
"""
if matches2 := re.search(r"^(.+), *(.+)$", name, re.IGNORECASE):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello again {name}")


"""
re.fullmatch(pattern: str | Pattern[str], string: str, flags: _FlagsType = 0) -> (Match[bytes] | None):
    - Try to apply the pattern to all of the string, returning a Match object, or None if no match was found.
"""

"""
re.match(pattern: str | Pattern[str], string: str, flags: _FlagsType = 0) -> (Match[str] | None):
    - Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found.
    - Can be used to validate email addresses, phone numbers etc
"""

"""
re.split(pattern: str | Pattern[str], string: str, maxsplit: int = 0, flags: _FlagsType = 0) -> list[str | Any]:
    - Split the source string by the occurrences of the pattern, returning a list containing the resulting substrings. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.
"""

"""
re.findall(pattern: str | Pattern[str], string: str, flags: _FlagsType = 0) -> list[Any]
    - Return a list of all non-overlapping matches in the string.
    - If one or more capturing groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group.
    - Empty matches are included in the result.
"""