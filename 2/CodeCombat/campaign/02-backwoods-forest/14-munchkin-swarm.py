loop:
    enemy = self.findNearestEnemy()
    if self.distanceTo(enemy) < 10:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
    else:
        self.attack("Chest")
    
