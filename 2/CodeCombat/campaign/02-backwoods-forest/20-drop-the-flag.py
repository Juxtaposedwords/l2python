# Put flags where you want to build traps.
# When you're not building traps, pick up coins!

loop:
    flag = self.findFlag()
    if flag:
        if self.findFlag("green"):
            self.pickUpFlag(flag)
            continue
        elif self.findFlag("black"):
            self.pickUpFlag(flag)
            self.buildXY("fire-trap", self.pos.x + 2, self.pos.y + 2)    
    else:
        item = self.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            self.moveXY(itemX, itemY)
