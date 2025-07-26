alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

alien = [alien_0, alien_1, alien_2]

for i in alien: 
    print(i)

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    alien.append(new_alien)

for i in alien[:5]:
    print(i)

print(f"total number of aliens: {len(alien)}")