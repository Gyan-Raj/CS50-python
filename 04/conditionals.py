x = int(input("Enter a number "))
y = int(input("Enter another number "))

# >,<,==
if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is smaller than {y}")
else:
    print(f"{x} is equal to {y}")


# or
if x < y or x > y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")


# !=
if x != y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")


# and
score = int(input("Enter your score: "))
if score >= 90 and score <= 100:
    print("You got Grade A")
elif score >= 80 and score < 90:
    print("You got Grade B")
elif score >= 70 and score < 80:
    print("You got Grade C")
elif score >= 60 and score <= 70:
    print("You got Grade D")
elif score >= 50 and score <= 60:
    print("You got Grade E")
else:
    print("You got Grade F")

# the code above can also be re-written as:
if 90 <= score <= 100:
    print("You got Grade A")
elif 80 <= score < 90:
    print("You got Grade B")
elif 70 <= score < 80:
    print("You got Grade C")
elif 60 <= score <= 70:
    print("You got Grade D")
elif 50 <= score <= 60:
    print("You got Grade E")
else:
    print("You got Grade F")

# the code above can also be re-written as:
if 90 <= score <= 100:
    print("You got Grade A")
elif score >= 80:
    print("You got Grade B")
elif score >= 70:
    print("You got Grade C")
elif score >= 60:
    print("You got Grade D")
elif score <= 50:
    print("You got Grade E")
else:
    print("You got Grade F")

print(80 <= score)  # will be True or False
print(score <= 80)  # will be True or False
