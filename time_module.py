import time

# ctime() convert a time expressed in seconds since epoch to a readable string
print(time.ctime(0))

# time() returns current time in seconds since epoch
print(time.time())

# combine ctime() and time() we can returns current time in a readable string
print(time.ctime(time.time()))

# localtime() returns a time object represent the current time
print(time.localtime())

# gmtime() returns the UTC time
print(time.gmtime())

# strftime() used to convert a time object to a formated string
print(time.strftime("%B %d %Y %H:%M:%S", time.localtime()))

# strptime() used to parse a formated string time to a time object
print(time.strptime("27 November 2024", "%d %B %Y"))

# asctime() and mktime() used to convert a tuple time to a time string
# tuple format (year, month, day, hour, minute, second, day of week, day of year, dst)
time_tuple = (2024, 11, 27, 11, 54, 00, 0, 0, 0)
print(time.asctime(time_tuple))
print(time.mktime(time_tuple))