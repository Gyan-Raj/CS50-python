import csv

name = input("Enter the name: ")
address = input("Enter the address: ")

with open("names.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, address])

# Now, again we can have similar problem like csv.reader where we were assuming that first row will always be name and second as address
# So, here again, we should use csv.DistWriter (09-csv package (csv.DictWriter))