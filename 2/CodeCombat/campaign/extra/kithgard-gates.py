# Build 3 fences to keep the ogres at bay!

self.moveDown()
self.buildXY("fence", 36, 34)

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

buildLocations = [[36, 30], [36, 26]]

for location in buildLocations:
    hammer('fence', location)

loop:
    simple_boots('right')
