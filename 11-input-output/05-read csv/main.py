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


print("\n---------------------Printing multiple comma separated values---------------------: ")
"""
# Create another file named names2.csv with entries like:
    Gyan,Bangalore, Karnataka
    Ritu,Balurghat, West Bengal
    Akshay,Bangalore, Karnataka
    Rajesh,Patna, Bihar
    Gayatri,Patna, Bihar
    Pratyaksha,Balurghat, West Bengal
Here, Gyan is name and Bangalore, Karnataks is the address
"""

members = []
with open("names2.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        members.append({"name": name, "address": address})

for member in members:
    print(f"{member["name"]} lives in {member["address"]}")

# For the code above, we will get ValueError (ValueError: too many values to unpack (expected 2, got 3))
"""
This happened because in the file, we have 2 commas, thus causing 3 entries. So, we now have to create entries something as:
    Gyan,"Bangalore, Karnataka"
    Ritu,"Balurghat, West Bengal"
    Akshay,"Bangalore, Karnataka"
    Rajesh,"Patna, Bihar"
    Gayatri,"Patna, Bihar"
    Pratyaksha,"Balurghat, West Bengal"
But, now we have to split it based on comma (,) which is not inside quptes ("")
So, to overcome this hectic logic and read csv file properly, we have a "csv" package which comes with python by default
"""
