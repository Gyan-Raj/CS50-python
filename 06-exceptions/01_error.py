# Syntax error
# print("Hi)


# Value Error
num_1 = int(input("Enter first number: "))
# Try entering a string (say "Gyan"), instead of a number, it will throw ValueError (ValueError: invalid literal for int() with base 10: 'Gyan')
print(f"First number is: {num_1}")


# To handle ValueError, we use try-except (similar to try-catch block)
# NameError
try:
    num_2 = int(input("Enter second number: "))
    print(f"Second number is: {num_2}")
except ValueError:
    print(f"Entered entity is not a number")


# NameError
# We can observe in the above code that the print(f"Entered number is: {num_2}") will not create any exception, as it is just priniting the valu, so we can move it out of the try block
try:
    num_3 = int(input("Enter third number: "))
except ValueError:
    print(f"Entered entity is not a number")
print(f"Third number is: {num_3}")


# The above code will give us NameError (NameError: name 'num_3' is not defined)
# To handle NameError, we use try-except-else
try:
    num_4 = int(input("Enter fourth number: "))
except ValueError:
    print(f"Entered entity is not a number")
else:
    print(f"Fourth number is: {num_4}")
