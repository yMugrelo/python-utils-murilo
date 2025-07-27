sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami', 'ham and cheese']
finished_sandwiches = []

print("the deli has run out pastrami ")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"i made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print('all sandwiches made : ')

for i in finished_sandwiches:
    print(f"\t - {i}")