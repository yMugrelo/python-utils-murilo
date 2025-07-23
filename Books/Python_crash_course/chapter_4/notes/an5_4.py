#simple statics with a list of number

numbers= []

for i in range(1, 11):
    number = input(f"enter the value {i} ")
    numbers.append(int(number))

print(f"the min term is: "+ f"{+ min(numbers)}")
print(f"the max term is: " + f"{+ max(numbers)}")
print(f"the sum is: " + f"{sum(numbers)}")