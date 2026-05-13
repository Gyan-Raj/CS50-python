# sys : system
# a.k.a. : command-line argument

import sys

# argv
print(sys.argv)  # This will print all the arguments in a list which we have written in the terminal while calling this file
# So, if we run this file as "python 03_sys.py", we will see ['03_sys.py'] in terminal
# Similarly, try running this file as: python 03_sys.py
print(f"You ran {sys.argv[0]}")


# But, if you try to run "python 03_sys.py Gyan"
print(f"Welcome {sys.argv[1]}")


# The following code will give IndexError: list index out of range
# print(f"Welcome {sys.argv[1]} {sys.argv[2]}")


# So, wrap it in try-exception
try:
    print(f"Welcome {sys.argv[1]} {sys.argv[2]}")
except:
    print("Too few arguments")


# Finally, run the script as "python 03_sys.py Gyan Raj"


# Or, we can make a check
if (len(sys.argv) < 3):
    print("Too few arguments")
elif (len(sys.argv) > 3):
    print("Too many arguments")
else:
    print(f"Welcome {sys.argv[1]} {sys.argv[2]}")


# NOTE: if we execute python 03_sys.py "Gyan Raj", then sys.argv[1] will be Gyan Raj (not just Gyan), because now "Gyan Raj" is inside quote, so it will be considered as one


# exit
if (len(sys.argv) < 3):
    sys.exit("Too few arguments")
elif (len(sys.argv) > 3):
    sys.exit("Too many arguments")
print(f"Welcome {sys.argv[1]} {sys.argv[2]}")
