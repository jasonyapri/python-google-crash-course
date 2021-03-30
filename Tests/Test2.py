def format_address(address_string):
    # Declare variables
    house_number = ""
    street_name = ""
    # Separate the address string into parts
    address_parts = address_string.split(" ")
    # Traverse through the address parts
    for i, address_part in enumerate(address_parts):
        if address_part.isnumeric():
            house_number = address_part
        else:
            if i != 1:
                street_name += " "
            street_name += address_part

    return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
