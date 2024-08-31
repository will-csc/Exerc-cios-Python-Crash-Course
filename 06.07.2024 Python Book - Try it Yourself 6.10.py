people_numbers = {
    "William": ["969541207", "953750340"],
    "Tamiles": ["953750340", "969541207"],
    "Casa Pais": "41494702",
    "Pai": ["958742089", "41494702"],
    "Mãe": ["931250560", "41494702"]
}

for key, value in people_numbers.items():
    if isinstance(value, list):
        print("Hello {0}! Your favorite numbers are {1} and {2}".format(key, value[0], value[1]))
    else:
        print("Hello {0}! Your favorite number is {1}".format(key, value))
