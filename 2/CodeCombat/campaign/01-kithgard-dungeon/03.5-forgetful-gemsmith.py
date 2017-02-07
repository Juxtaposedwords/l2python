# Grab the gems and go to the exit.

def simple_boots(move):
    if move == 'right':
        self.moveRight()
    elif move == 'left':
        self.moveLeft()
    elif move == 'up':
        self.moveUp()
    elif move == 'down':
        self.moveDown()

orders = ['right','up','right','right', 'down','down','up','right']

for order in orders:
    simple_boots(order)
