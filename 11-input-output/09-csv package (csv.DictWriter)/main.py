import csv

"""
# Create a file named names.csv with column names
    name,address
"""

name = input("Enter the name: ")
address = input("Enter the address: ")

with open("names.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "address"])
    writer.writerow({"name": name, "address": address}, )
