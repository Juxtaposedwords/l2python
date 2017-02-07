# Only attack enemies of type "munchkin" and "thrower".
# Don't attack a "burl". Run away from an "ogre"!
loop:
    enemy = self.findNearestEnemy()
    if not enemy or enemy.type == "burl" :
        self.moveXY(19,25)
        continue
    elif enemy.type == "thrower"  or enemy.type == "munchkin": 
        self.attack(enemy)
    elif enemy.type == "ogre" :
        self.moveXY(40, 47)
