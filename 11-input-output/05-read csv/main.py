"""
# create names.csv file before running this file and write this in it:
    Gyan,33
    Akshay,32
    Ritu,34
    Rajesh,61
    Gayatri,64
    Pratyaksha,0.75
"""

with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is {row[1]} years old")


# Instead of having row and then row[0] or row[1], we can destructure it with a variable name as:
print("\n---------------------Destructured---------------------: ")
with open("names.csv") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        print(f"{name} is {age} years old")


# To sort, we can also do this again by creating a list of dictionaries and sort it
# NOTE: sorted() also takes "key" as parameter based on which a list will be sorted
print("\n---------------------Sorting based on name---------------------: ")


def get_name(member):
    return member["name"]


members = []
with open("names.csv") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        member = {"name": name, "age": age}
        members.append(member)

# NOTE: we are not calling (get_name()), we are just mentioning it (get_name), becuase sorted fucntion automatically callsit
for member in sorted(members, key=get_name):
    print(f"{member["name"]} is {member["age"]} years old")


print("\n---------------------Sorting based on age---------------------: ")


def get_age(member):
    return member["age"]


for member in sorted(members, key=get_age):
    print(f"{member["name"]} is {member["age"]} years old")


# If we wan to avoid creating a funciton which is to be passed as a key, then we can use "lambda" keyword followed by an anonymous funciton as:
print("\n---------------------Sorting using lambda---------------------: ")
# NOTE: we can write the anonymous funciton as: anything:anything["name"]
for member in sorted(members, key=lambda s: s["name"]):
    print(f"{member["name"]} is {member["age"]} years old")

print("\n---------------------Sorting using lambda (for age)---------------------: ")
for member in sorted(members, key=lambda s: s["age"]):
    print(f"{member["name"]} is {member["age"]} years old")
