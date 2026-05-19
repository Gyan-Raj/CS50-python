# enumerate gives access to the index as well as the element of a list

members = ["Rajesh Nandan Kumar", "Gayatri Kumari",
           "Ritu Raj", "Gyan Raj", "Akshay Raj", "Pratyaksha"]

for i, mem in enumerate(members):
    print(i+1, mem)
