usernames = ["Yufeng", "Jane", "Steven"]
passwords = ("abc123", "guess", "p@ssword")
login_date = ["1/1/2024", "3/8/2023", "6/6/2016"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)