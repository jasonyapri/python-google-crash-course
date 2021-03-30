friends = ['Taylor', 'Alex', 'Pat', 'Alex', 'Eli']
for i, friend in enumerate(friends):
    if (i != len(friends)-1):
        print("Hi " + friend, end = ", ")
    else:
        print("Hi " + friend, end = ".\n")

print("=====")

print("15 modulo 4 = " + str(15%4))

print("=====")

def hint_username(username):
    if len(username) < 3:
        print("Must be at least 3 characters long")
    elif len(username) > 15:
        print("Must be at most 15 characters long")
    else:
        print("Valid username")

hint_username("jason_yapri")

print("=====")

truth = False

if not truth:
    print("Not True")

print("=====")

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x+1
print("x = " + str(x))

print("=====")

product = 1
for n in range(1, 10):
    product *= n

print("Factorial of 10 is " + str(product))

print("=====")

for x in range(0, 101, 10):
    print(x)
    
print("=====")

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" +str(right) + "]", end = " ")
    print()
    
print("=====")

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if (home_team != away_team):
            print(home_team + " vs " + away_team)
    print()
    
print("=====")

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

print("Factorial of 8 is " + str(factorial(8)))

print("=====")

for x in range(10):
    for y in range(x):
        print(y, end="\t")
    print()

print("=====")

for x in range(1, 10, 3):
    print(x)
    
print("=====")