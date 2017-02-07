# The commands below an if statement only run when the if's condition is true.
# Fix all the if-statements to beat the level.

# == means "is equal to".
if 1 + 1 + 1 != 3:
    self.moveXY(5, 15)  # Move to the first mines.

if 2 + 2 != 5:
    self.moveXY(15, 40)  # Move to the first gem.

# != means "is not equal to".
if 2 + 2 == 4:
    self.moveXY(25, 15)  # Move to the second_gem.
    
# < means "is less than".
if 2 + 2 > 3:
    enemy = self.findNearestEnemy()
    self.attack(enemy)

if 2 > 4:
    self.moveXY(40, 55)

if False:
    self.moveXY(50, 10)

if True:
    self.moveXY(55, 25)

