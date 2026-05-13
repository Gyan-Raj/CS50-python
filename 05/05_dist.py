# dict : (dictionary) is a datatype in python (similar ot object with key value pairs)
web_series = {
    "GOT 1": "Jio Hotstar",
    "GOT 2": "Jio Hotstar",
    "GOT 3": "Jio Hotstar",
    "Panchayat 1": "Amazon Prime",
    "Panchayat 2": "Amazon Prime",
}

for series in web_series:
    print(series)       # This will print the key names of the dict

for series in web_series:
    print(series, web_series[series], sep=" on ")
