# Integer:

x = input("Enter first number ")
y = input("Enter second number ")
z = x + y
# 22: Because it is doing string concatination
print(f"Summation of {x} and {y} is", z)

p = int(x)+int(y)
print(f"Summation of {x} and {y} is", p)

a = int(input("Enter first number "))
b = int(input("Enter second number "))
c = a + b
print(f"Summation of {a} and {b} is", c)


# Float and round:
print(1.3 + 1.4)  # 2.7
print(round(1.3 + 1.4))  # 3 (2.7 rounded off to 3)
# 2 (2.5 rounded off to 2) => it rounds to the nearest even number
print(round(1.3 + 1.2))
# 6 (5.5 rounded off to 6) => it rounds to the nearest even number
print(round(3.2 + 2.3))
# 0 (0.5 rounded off to 0) => it rounds to the nearest even number
print(round(0.5 + 0))
float_x = float(input("Enter first decimal number "))
float_y = float(input("Enter first decimal number "))
floated_sum = float_x+float_y
print(f"Sum of {float_x} and {float_y} is: {floated_sum}")
print(
    f"Rounded off sum of {float_x} and {float_y} to its nearest integer value is: {round(floated_sum)}")

print(2/3)
print(round(2/3))
print(round(2/3, 5))  # 0.66667 rounded off till 5 decimals
print(round(1/2))  # 0 (0.5 is rounded off to the nearest even number i.e., 0)
print(round(1/2, 5))  # 0.5

z = 2/3
print(f"{z:.5f}")  # 0.66667 rounded off till 5 decimals
