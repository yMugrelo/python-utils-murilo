foods = ['pizza', 'falafel', 'carrot cake','ice cream', 'cannoli', 'rice and beans', 'beef']


##Print the message The first three items in the list are:. Then use a slice to
##print the first three items from that program’s list.
print("the first 3 foods in the list")
for i in foods[:3]:
    print(i)

print("\n")

print("The 3 in the middle: \n")
for i in foods[2:5]:
    print(i)


##Print the message The last three items in the list are:. Use a slice to print the
##last three items in the list
print("\n")
print("the last 3 foods: \n")

for i in foods[4:]:
    print(i)