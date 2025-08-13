class car:
    def __init__(self, make, model, year ):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive(self):
        long_name = f'{self.model}, {self.make}, {self.year}'
        return long_name.title()
    
my_new_car = car('audi', 'A4', 2018)
print(my_new_car.get_descriptive())