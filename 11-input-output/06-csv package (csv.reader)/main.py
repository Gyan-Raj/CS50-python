# csv package is provided by python by default
import csv


members = []
with open("names.csv") as file:
    reader = csv.reader(file)
    for name, address in reader:
        members.append({"name": name, "address": address})


for member in sorted(members, key=lambda mem: mem["name"]):
    print(f"{member["name"]} lives in {member["address"]}")

"""
We can mention in csv file at top the column names that we want and use csv.DictReader which will give us the names at top (07-csv package (csv.DictReader))
"""
