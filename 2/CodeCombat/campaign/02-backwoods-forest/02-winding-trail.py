# Use your moveXY(x, y) function.

def leather_boots(coordinates):
    self.moveXY(coordinates[0], coordinates[1])


def hammer(type, coordinates):
    self.buildXY(type,coordinates[0],coordinates[1])


# The hash has to be devoid of new lines or else the code won't run
orders = [ {'action': 'move', 'coordinates': [35, 60]}, {'action': 'move', 'coordinates': [36, 13]}, {'action': 'build', 'coordinates': [71, 25], 'type': 'fence'} ]

for order in orders:
    if order['action'] == 'move':
        leather_boots(order['coordinates'])
    elif order['action'] == 'build':
        hammer(order['type'], order['coordinates'])
