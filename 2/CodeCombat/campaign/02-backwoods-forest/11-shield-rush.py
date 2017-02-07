loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave") and enemy:
        self.cleave(enemy)    
    elif self.isReady("shield") and enemy:
        self.shield()  
    else:
        self.moveXY(57,33)

