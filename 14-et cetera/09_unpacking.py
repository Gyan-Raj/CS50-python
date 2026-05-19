# unpacking is similar to spread operator in javascript
# In javscript, we have "...", while in python we have "*"

def total(phy, chem, maths):
    return phy + chem + maths


marks = [80, 83, 93]
print(f"Total marks using indexing: {total(marks[0], marks[1], marks[2])}")
print(f"Total marks using unpacking: {total(*marks)}")


# To unpack dictionaries, we use "**"
marks_dict = {
    "phy": 80,
    "chem": 83,
    "maths": 93
}
print(
    f"Total marks using dictionaries: {total(marks_dict["phy"], marks_dict["chem"], marks_dict["maths"])}")
print(
    f"Total marks using unpacking dictionaries: {total(**marks_dict)}")
