# filter takes 2 arguments: funtion to be executed and the list on which that function will be executed for its each element


members = [
    {
        "name": "Rajesh Nandan Kumar",
        "job": "Retired Statistical Asst. (Bihar govt.)",
        "place": "Bihar"
    },
    {
        "name": "Gayatri Kumari",
        "job": "Retired school teacher (Bihar govt.)",
        "place": "Bihar"
    },
    {
        "name": "Ritu Raj",
        "job": "Branch Manager (Indian Bank)",
        "place": "West Bengal"
    },
    {
        "name": "Gyan Raj",
        "job": "Software Developer (Testyantra Software Solutions Pvt Ltd)",
        "place": "Karnataka"
    },
    {
        "name": "Akshay Raj",
        "job": "Business Analyst (System Domain)",
        "place": "Karnataka"
    },
]


def is_kannadiga(member):
    return member["place"].lower() == "karnataka"


kannadigas = filter(is_kannadiga, members)

for mem in kannadigas:
    print(mem["name"])

# <filter object at 0x0000015550795D20>
print("Living in karnataka:", kannadigas)

"""
- filter() does not immediately return a list.
- That is why we are seeing output for "print("Living in karnataka:", kannadigas)" something as: <filter object at 0x0000015550795D20>
- kannadigas = filter(is_kannadiga, members) creates a lazy iterator. It means:
    “I know how to produce filtered values one-by-one when needed.”
- Python does this for memory efficiency.
- Why Loop Works?
    for mem in kannadigas:
        print(mem["name"])
  Because, the loop consumes the iterator.
- If you want actual values:
    kannadigas = list(filter(is_kannadiga, members))
"""
kannadigas = list(filter(is_kannadiga, members))
print("Living in karnataka:", kannadigas)

# in a shorter version, we can also write as:

bengalis = filter(lambda s: s["place"].lower() == "west bengal", members)
bengalis = list(bengalis)
print("Living in West Bengal:", bengalis)
