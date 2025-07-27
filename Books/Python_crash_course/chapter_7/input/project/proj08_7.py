sandwich_orders = ['tuna', 'chicken', 'veggie', 'ham and cheese', 'bacon']

finished = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich")
    finished.append(current_sandwich)

print("\nall sandwiches made: ")
for sandwich in finished:
    print(f"\t - {sandwich} sandiwich")