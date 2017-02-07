# Remember that enemies may not yet exist.
enemy = self.findNearestEnemy()
loop:
    enemy = self.findNearestEnemy()
    if not enemy:
        continue
    self.attack(enemy)
