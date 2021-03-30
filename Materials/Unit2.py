

color = "Orange"
print(color[1:4])   #index 1 - 3

fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])
print(fruit[-6:-2])

print("=====")

message = "A kong string with a silly typo"
#Error: message[2] = "l"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

print("-----")

pets = "Cats & Dogs"
print(pets.index("&"))

print("=====")

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email

print(replace_domain("jason.yapri@yahoo.com", "yahoo.com", "gmail.com"))

print("=====")

answer = "    YES "
if answer.strip().lower() == "yes": # Opposite answer.upper()
    print("User said yes")

# "  yes".lstrip() left strip
# "yes  ".rstrip() RIght Strip
# "This is a number four".count("i")
# "Forest".endswith("rest")
# "12345".isnumeric() -> int("12345") + int("5321")
# "abcdef".isalpha()
# " ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
# "This is another example".split()
# string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
print("See https://docs.python.org/3/library/stdtypes.html#string-methods for more String methods")

print("=====")

name = "Yunita"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number)) # We don't need to cast as format function dealt with that already

print("=====")

x = 1
y = 2
print("Your lucky number is {a}, {b}".format(a = x, b = y*3))

print("=====")

price = 7.5
price_with_tax = price * 1.09
print(price, price_with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, price_with_tax)) # Print 2 decimal-placed float number

print("=====")

def to_celcius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x))) # Aligned text with >[aligned character]

print("=====")


