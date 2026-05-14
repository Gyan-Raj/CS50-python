"""
# create names.txt file before running this file and write this in it:
    Gyan
    Akshay
    Ritu
    Rajesh
    Gayatri
    Pratyaksha
"""

with open("names.txt", "r") as file:
    for line in file:
        print(line)
# "r" is for read


# In the above code, we see that we have an extra line (empty line) between lines (one due to the \n in file and one due to default value of "end=\n" in print function), to solve this, we can either do print(line, end=""), but a better way is to strip \n from file itself
print("\n---------------------Content after stripping---------------------: ")
with open("names.txt", "r") as file:
    for line in file:
        print(line.rstrip())


# To sort the content, we can sreate a temporary list, append the lines, sort it and then print it:
print("\n---------------------Sorted content---------------------:")
list = []
with open("names.txt") as file:  # NOTE: default second parameter of open() funciton is read, i.e., "r", so we don;t have to write it explicitly
    for line in file:
        list.append(line)

for line in sorted(list):
    print(f"{line.rstrip()}")


# We can sort the content directly in the content and print it (no need of creating list variable)
print("\n---------------------Sort within file---------------------:")
with open("names.txt") as file:
    for line in sorted(file):
        print(f"{line.rstrip()}")


# We can sort it in reverse order as well
print("\n---------------------Sort in reverse order---------------------:")
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"{line.rstrip()}")