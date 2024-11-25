store = [
    ("T-shit", 20.00),
    ("Pants", 10.00),
    ("Hats", 5.00)
]

# to USD to EUR
to_euros = lambda data : (data[0], data[1] * 0.82)

euros_store = list(map(to_euros, store))

for i in euros_store:
    print(i)
