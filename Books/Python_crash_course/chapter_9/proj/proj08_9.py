class User:
    def __init__(self, first_name, last_name, age, email, location, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.username = username
        self.password = password

    def describe_user(self):
        print("here is your information\n ")
        print(f"User's name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
    
    def attempt_password(self):
        entered_user = input("please enter your user: ")
        entered_password = input("enter your password: ")   
        while True:
            if entered_user == self.username and entered_password == self.password:
                print(" Login successful!")
                break
            else:
                print("enter a valid username and password ")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.\n ")
class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, username, password):
        super().__init__(first_name, last_name, age, email, location, username, password)
        self.privilages = [
            "can add a post",
            "can delete a post", 
            "can ban user"
        ]
    def show_privileges(self):
        print("admin privileges: ")
        for i in self.privilages:
            print(f"- {i}")
    
    def attempt_password_adm(self):
        entered_admin_pass = input("please enter your admin username: ")
        

admin = [
    Admin("Super", "User", 40, "admin@email.com", "Headquarters", "admin", "root123")
]
users = [
    User("Alice", "Johnson", 28, "alice@email.com", "New York", "alicej", "1234"),
    User("Bob", "Smith", 35, "bob@email.com", "London", "bobsmith", "abcd"),
    User("Carol", "Silva", 22, "carol@email.com", "São Paulo", "carol22", "senha123")
]

login_attempt = 1
while True:
    username_input = input("enter your user: ")
    password_input = input("Password: ")
    found_user = None
    
    for user in users:
        
        if user.username == username_input and user.password == password_input:
            found_user = user
            break
    if found_user:
        found_user.greet_user()
        found_user.describe_user()
        break
    else:
        print("user or password dont found!! ")
        login_attempt += 1

if login_attempt == 1:
    print(f"you tried just {login_attempt} time")
else:
    print(f"you tried {login_attempt} times")



