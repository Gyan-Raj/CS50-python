# set is used to remove duplicates
# set.add(<element>) will add that element to the set

members = [
    {
        "name": "Gyan Raj",
        "address": "Karnataka"
    },
    {
        "name": "Ritu Raj",
        "address": "West Bengal"
    },
    {
        "name": "Pratyaksha",
        "address": "West Bengal"
    },
    {
        "name": "Akshay Raj",
        "address": "Karnataka"
    },
    {
        "name": "Gayatri Kumari",
        "address": "Bihar"
    },
    {
        "name": "Rajesh Nandan Kumar",
        "address": "Bihar"
    },
]

# addresses = []
# for member in members:
#     if member["address"] not in addresses:
#         addresses.append(member["address"])

# Instead of having a list and doing the uniqueness checking manually, we can use set as:

addresses = set()
for member in members:
    addresses.add(member["address"])


for address in sorted(addresses):
    print(address)
