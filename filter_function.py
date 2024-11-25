friends = [
    ("Yufeng", 40),
    ("Jane", 38),
    ("Steven", 10)
]

age = lambda data : data[1] > 17

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)