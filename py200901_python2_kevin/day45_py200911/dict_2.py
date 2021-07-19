"""
dict2
key
"""


dict1 = {
    1: "value1",
    2: "Value2",
    3: "value3",
    # ....
    1000: "value1000"
}

dict2 = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}

dict2_fr = {
    "mon": "Lundi",
    "tue": "Mardi",
    "wed": "Mercredi",
    "thu": "Jeudi",
    "fri": "Vendredi",
    "sat": "Samedi",
    "sun": "Dimanche"
}


for i in dict2:
    print(dict2[i])

for i in dict2_fr:
    print(dict2_fr[i])
