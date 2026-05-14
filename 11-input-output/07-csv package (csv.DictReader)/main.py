# csv package is provided by python by default
import csv


members = []
with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # NOTE: in row["name"] and row["address"], "name" and "address" are the column names in the csv file
        members.append({"name": row["name"], "address": row["address"]})


for member in sorted(members, key=lambda mem: mem["name"]):
    print(f"{member["name"]} lives in {member["address"]}")

"""
# This approach will always work even when we reverse the columns in names.csv file (as the "name" and "address" column names will still match)
# So even when we have data like:
address,name
"Bangalore, Karnataka",Gyan
"Balurghat, West Bengal",Ritu
"Bangalore, Karnataka",Akshay
"Patna, Bihar",Rajesh
"Patna, Bihar",Gayatri
"Balurghat, West Bengal".Pratyaksha
"""

# The code below is literally the same as above, just that we changed the file name from names.csv to names2.csv
members = []
with open("names2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        members.append({"name": row["name"], "address": row["address"]})

for member in sorted(members, key=lambda mem: mem["name"]):
    print(f"{member["name"]} lives in {member["address"]}")
