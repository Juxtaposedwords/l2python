# Build two fences to keep the villagers safe!
# Hover your mouse over the world to get X,Y coordinates.

# Now begins user created code:

def simple_boots(move):
    if move == 'right':
        self.moveRight()
    elif move == 'left':
        self.moveLeft()
    elif move == 'up':
        self.moveUp()
    elif move == 'down':
        self.moveDown()


def hammer(type, coordinates):
    self.buildXY(type,coordinates[0],coordinates[1])

buildLocations = [[40, 53], [40, 20]]

for location in buildLocations:
    hammer('fence', location)
