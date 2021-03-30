class Apple:
    pass

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)

print("=====")

class Piglet:
    """Represents a piglet that can say their name"""
    name = "Piglet"
    years = 0

    # def __init__(self, name, years):
    #     self.name = name
    #     self.years = years

    def __str__ (self):
        return "This Piglet's name is {} and it's {} years old".format(self.name, self.years)

    def speak(self):
        print("oink! Hi, I'm, {}".format(self.name))

    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()
print(petunia)
