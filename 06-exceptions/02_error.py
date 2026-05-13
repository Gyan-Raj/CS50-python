while True:
    try:
        num_1 = int(input("Enter first number: "))
    except ValueError:
        print("Entered entity is not a number")
    else:
        break

print(f"Entered number is {num_1}")


# If we don't want to handle error (in except statement), we can "pass"
while True:
    try:
        num_2 = int(input("Enter second number"))
    except ValueError:
        # print("Entered entity is not a number")
        pass # This will keep in loop but will not show any print statement
    else:
        break