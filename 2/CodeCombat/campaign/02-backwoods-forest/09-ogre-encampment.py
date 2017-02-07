# Stay in the middle and defend!

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        self.attack(enemy)
    else:
        self.attack("Chest")
