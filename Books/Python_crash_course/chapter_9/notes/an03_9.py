class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model} {self.year}"
        return long_name.title()
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it. ")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("you cant roll back an odometter! ")
    def increment_mileage(self, mileage):
        self.odometer_reading += mileage     
    

class Eletric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 100
    def describe_battery(self):
        print(f"this car has a {self.battery_size} - KWh battery. ")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            print(f"this car can go {range} miles in full tank")

my_tesla = Eletric_car('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.get_range()