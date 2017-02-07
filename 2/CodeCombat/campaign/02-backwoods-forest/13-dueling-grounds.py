# Defeat the enemy hero in a duel!
enemy = self.findNearestEnemy()
trap = 0
loop:
    if self.distanceTo(enemy) <= 3 and self.isReady("cleave"):
        self.cleave(enemy)
    elif self.distanceTo(enemy) <= 3 and self.isReady("shield"):
        self.shield()
    else: 
        if trap == 0:
            self.moveXY(44, 19)
            self.moveXY(61, 27)
            self.moveXY(70, 17)
            trap = 1
        else:
            self.attack(enemy)

