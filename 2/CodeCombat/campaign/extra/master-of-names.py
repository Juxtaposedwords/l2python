# Your hero doesn't know these enemy's names!
# The glasses give you the findNearestEnemy ability.

enemy1 = self.findNearestEnemy()
self.attack(enemy1)
self.attack(enemy1)

enemy2 = self.findNearestEnemy()
self.attack(enemy2)
self.attack(enemy2)

def simple_boots(move):
    if move == 'right':
        self.moveRight()
    elif move == 'left':
        self.moveLeft()
    elif move == 'up':
        self.moveUp()
    elif move == 'down':
        self.moveDown()


def longsword(target):
    self.attack(target)


def attackNearest():
    enemy = self.findNearestEnemy()
    longsword(enemy)
    longsword(enemy)
while 1 == 1 :
    attackNearest()
