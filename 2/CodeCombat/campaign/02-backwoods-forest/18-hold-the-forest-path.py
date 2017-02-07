# Use flags to join the battle or retreat.

def kitingStatus():
    enemy = self.findNearestEnemy()
    if enemy and self.distanceTo(enemy) < 7 :
        return True
    else:
        return False

kiting = False
loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag()
    path = [[26, 35], [26, 41],[26,43], [26,45], [26, 48], [26,50] ]
    if flag:
        if self.findFlag("green"):
            self.pickUpFlag(flag)
            continue
        elif self.findFlag("black"):
            self.buildXY("fire-trap", self.pos.x + 2, self.pos.y + 2)
            continue
            
    for waypoint in path:
        if kitingStatus():
            self.moveXY(26, 25)
        else:
            self.moveXY(waypoint[0],waypoint[1])

