name = input("Enter your full name ")
age = input("Enter your age ")
print("Hi " + name)
print("Hi", name)
print(f"You're {name} - {age} years old")  # f: format string


# Print has other names parameters like sep (fefault is " ") and end (default is "\n")
print("Hello", sep="yyyyyyyyy", end="xxxxx")
print("World")


company_name = input("Enter your company name ").strip().title()
print(f"{name} works in {company_name}")

first_name, last_name = name.strip().title().split()
print(f"That's all in this lecture {first_name}")
