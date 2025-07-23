my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are: ")
for i in my_foods:
    print(i)

print("\n")
print("my friends favorite foods are: ")
for i in friend_foods:
    print(i)