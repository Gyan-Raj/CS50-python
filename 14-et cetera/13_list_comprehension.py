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


kannadigas = [member["name"]
              for member in members if member["place"] == "Karnataka"]

print("Living in karnataka:", kannadigas)
