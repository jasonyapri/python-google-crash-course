fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits.insert(0, "Orange")
print(fruits)

fruits.remove("Melon")
print(fruits)

print(fruits.pop(3))
print(fruits)

fruits[2] = "Strawberry"
print(fruits)

print("=====")

def convert_seconds(seconds):
    hours = seconds //3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(type(result))
print(result)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)

print("=====")

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

print("=====")

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([
    ("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")
]))

print("=====")

multiples = []

for x in range(1, 11):
    multiples.append(x*7)
print(multiples)

print("=====")

multiples = [x*7 for x in range(1, 11)]
print(multiples)

z = [x for x in range(1, 101) if x % 3 == 0]
print(z)

z = [ x*2 for x in range(1,11) ]
print("Multiplication of 2 from 1 to 10: ",str(z))

print("=====")

# list.append(x) Inserts x at the end of the list
# list.insert(i, x) Inserts x at index i
# list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
# list.remove(x) Removes the first occurrence of x in the list
# list.sort() Sorts the items in the list
# list.reverse() Reverses the order of items of the list
# list.clear() Removes all the items of the list
# list.copy() Creates a copy of the list
# list.extend(other_list) Appends all the elements of other_list at the end of list

print("=====")

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)

file_counts["cfg"] = 8
file_counts["csv"] = 17
print(file_counts)

del file_counts["cfg"]
print(file_counts)

print("=====")

for ext, amount in file_counts.items(): # each iteration returns a tuple (ext, amount)
    print("There are {} files with the .{} extension".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())

print("=====")

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("Swiss German University"))

# you can use any immutable data type; numbers, booleans, strings and tuples as dictionary keys.

### Dictionary Cheat Sheet
## Operations

# len(dictionary) - Returns the number of items in the dictionary
# for key in dictionary - Iterates over each key in the dictionary
# for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
# if key in dictionary - Checks whether the key is in the dictionary
# dictionary[key] - Accesses the item with key key of the dictionary
# dictionary[key] = value - Sets the value associated with key
# del dictionary[key] - Removes the item with key key from the dictionary
# Methods

# dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
# dict.keys() - Returns a sequence containing the keys in the dictionary
# dict.values() - Returns a sequence containing the values in the dictionary
# dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
# dict.clear() - Removes all the items of the dictionary