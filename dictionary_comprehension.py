# convert a temperature dictionary from F to C
cities_in_F = {"Toronto": 32, "Vancouver": 75, "Calgary": 100, "Edmonton": 50}

cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}

print(cities_in_C)

# filter the items in a condition

weather = {"Toronto": "Sunny", "Vancouver": "Raining", "Calgary":"Sunny", "Edmonton":"Cloudy"}

sunny_weather = {key:value for (key, value) in weather.items() if value == "Sunny"}

print(sunny_weather)

# convert temperature to description
desc_cities = {key: "WARM" if value >= 40 else "COLD" for (key, value) in cities_in_F.items()}
print(desc_cities)

# convert temperature to description using function
def check_temperature(value):
    if value >= 75:
        return "HOT"
    elif 75 > value >= 40:
        return "WARM"
    else:
        return "COLD"

desc_cities2 = {key: check_temperature(value) for (key, value) in cities_in_F.items()}
print(desc_cities2)
