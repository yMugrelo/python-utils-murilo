class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

restaurant1 = Restaurant("Mountain Flavor", "homestyle food")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Pasta Paradise", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
