class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

class Ice_cream(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for i in self.flavors:
            print(f"- {self.flavors}")

my_icecream_stand = Ice_cream(
    "Cool Cones", 
    "Ice Cream", 
    ["Vanilla", "Chocolate", "Strawberry", "Mint"]
)
my_icecream_stand.describe_restaurant()
my_icecream_stand.open_restaurant()
my_icecream_stand.display_flavors()