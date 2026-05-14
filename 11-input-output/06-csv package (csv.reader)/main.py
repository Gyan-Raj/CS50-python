# csv package is provided by python by default
import csv


members = []
with open("names.csv") as file:
    reader = csv.reader(file)
    for name, address in reader:
        members.append({"name": name, "address": address})


for member in sorted(members, key=lambda mem: mem["name"]):
    print(f"{member["name"]} lives in {member["address"]}")
