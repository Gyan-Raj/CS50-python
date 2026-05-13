series = input("Enter the series: ")
if series == "GOT 1":
    print(f"You can watch {series} on Jio Hotstar")
elif series == "GOT 2":
    print(f"You can watch {series} on Jio Hotstar")
elif series == "GOT 3":
    print(f"You can watch {series} on Jio Hotstar")
elif series == "Panchayat 1":
    print(f"You can watch {series} on Amazon Prime")
elif series == "Panchayat 2":
    print(f"You can watch {series} on Amazon Prime")
else:
    print(f"Sorry, no data found about {series}")


# The above code has repeated output for GOT 1, GOT 2, GOT 3 and Panchayat 1, Panchayat 2, so we can rewrite the code as:
if series == "GOT 1" or series == "GOT 2" or series == "GOT 3":
    print(f"You can watch {series} on Jio Hotstar")
elif series == "Panchayat 1" or series == "Panchayat 2":
    print(f"You can watch {series} on Amazon Prime")
else:
    print(f"Sorry, no data found about {series}")


# A more better way is by using "match" (which is similar to switch-case statements)
match series:
    case "GOT 1" | "GOT 2" | "GOT 3":
        print(f"You can watch {series} on Jio Hotstar")
    case "Panchayat 1" | "Panchayat 2":
        print(f"You can watch {series} on Amazon Prime")
    # NOTE: instead of "default" as in switch-case statements, we use "_"
    case _:
        print(f"Sorry, no data found about {series}")
