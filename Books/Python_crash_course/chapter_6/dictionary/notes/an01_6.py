alien = {
    'color': 'green',
    'points': 5
}
print(alien['color'])
print(alien['points'])
print(alien)

alien['x_position'] = 0
alien['y_position'] = 10 
print(alien)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print(f"the alien color is: {alien['color']}")

alien['color'] = 'grey'
print(f"the new color is {alien['color']}")

del alien_0['points']
print(alien_0)

