class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User's name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

user1 = User("Charles", "Xavier", 55, "charles.x@example.com", "New York")
user2 = User("Jean", "Grey", 30, "jean.g@example.com", "Los Angeles")
user3 = User("Scott", "Summers", 35, "scott.s@example.com", "Chicago")

for u in [user1, user2, user3]:
    u.describe_user()
    u.greet_user()
    print()  
