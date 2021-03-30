import random
import datetime

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

print("=====")

now = datetime.datetime.now()
print(now)
print(type(now))
print(now.year,now.month,now.day)

print(now + datetime.timedelta(days=28))

