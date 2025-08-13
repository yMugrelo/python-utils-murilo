class dog:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def sit(self):
        print(f"{self.name} is now sitting \n ")

    def roll_over(self):
        print(f'{self.name} rolled over! ')

my_dog = dog('willie', 5)
my_dog.sit()
my_dog.roll_over()

print(f"my dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")