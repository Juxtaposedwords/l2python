# Use your new "cleave" skill as often as you can.

self.moveXY(23, 23)
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave") and enemy:
        self.cleave(enemy)        
    else:
        self.attack(enemy)
