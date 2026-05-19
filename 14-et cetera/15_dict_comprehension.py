members = ["Rajesh Nandan Kumar", "Gayatri Kumari",
           "Ritu Raj", "Gyan Raj", "Akshay Raj", "Pratyaksha"]

# This is list comprehension, we have already learnt this in (12_list_comprehension and 13_list_comprehension)
title_list = [{"name": mem, "title": "Mishra"} for mem in members]

# This is dictionary comprehension
title_dict = {mem: "Mishra" for mem in members}


print(title_list)
print(title_dict)
