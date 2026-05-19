# unpacking is similar to spread operator in javascript
# In javscript, we have "...", while in python we have "*"

def total(phy, chem, maths):
    return phy + chem + maths


marks = [80, 83, 93]
print(f"Total marks: {total(*marks)}")
