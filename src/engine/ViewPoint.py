#!/usr/bin/env python
""" generated source for module ViewPoint """

# 
#  * This controls what you can see in game (on the map) and moving around along it.
#  * Place MoveView(); in the game-loop (100ms) to automate it (Teleporting across the map between switching viewed units / turns is automatic)
#  * Use Viewable(x,y); to check if something can be seen on screen and ViewX(); / ViewY(); to grab the offsets (in case it changes from a direct copy + paste).
#  * @author SergeDavid
#  * @version 0.2
#  
class ViewPoint(object):
    """ generated source for class ViewPoint """
    Loc = [0, 0]

    # Location of the viewpoint
    expanded = 3

    # This is the max distance from the edge of the map that the viewpoint can go.
    speed = 1
    width = 20

    # How wide / tall the viewpoint is (how far from the x/y should the )
    height = 12

    # 
    # 	 * Place this in a the game loop (100ms) to update the view-port automatically.
    # 	 * Currently it does not support speeds other then 1.0 (You'll get a mostly never ending +1/-1 view-port shake)
    # 	 
    def MoveView(self):
        """ generated source for method MoveView """
        y = 0
        x = 0
        if Game.GameState == Game.State.PLAYING:
            y = Game.player.get(Game.btl.currentplayer).selecty
            x = Game.player.get(Game.btl.currentplayer).selectx
        else:
            y = Game.edit.selecty
            x = Game.edit.selectx
        MoveNorth(y)
        MoveSouth(y)
        MoveEast(x)
        MoveWest(x)

    # 
    # 	 * This is a check to see if something in the game map is viewable on screen.
    # 	 * @param x = x location of unit/building/tile to compare
    # 	 * @param y = y location of object to compare
    # 	 * @return = True when in view range, false when outside of it. (saves time so you don't have to render images)
    # 	 
    def Viewable(self, x, y):
        """ generated source for method Viewable """
        if y >= self.Loc.y and y < self.Loc.y + self.height:
            if x >= self.Loc.x and x < self.Loc.x + self.width:
                return True
        return False

    # 
    # 	 * Simple lame getter.
    # 	 * @return X location of view-port to offset anything being drawn on the map.
    # 	 
    def ViewX(self):
        """ generated source for method ViewX """
        return self.Loc.x

    # 
    # 	 * Simple lame getter.
    # 	 * @return Y location of view-port to offset anything being drawn on the map.
    # 	 
    def ViewY(self):
        """ generated source for method ViewY """
        return self.Loc.y

    # These move the viewpoint in the correct direction at a set speed, used internally through MoveView();
    def MoveNorth(self, y):
        """ generated source for method MoveNorth """
        if y < self.Loc.y + self.expanded:
            self.Loc.y -= self.speed

    def MoveSouth(self, y):
        """ generated source for method MoveSouth """
        if y > self.Loc.y + self.height - self.expanded:
            self.Loc.y += self.speed

    def MoveEast(self, x):
        """ generated source for method MoveEast """
        if x < self.Loc.x + self.width - self.expanded:
            self.Loc.x -= self.speed

    def MoveWest(self, x):
        """ generated source for method MoveWest """
        if x > self.Loc.x + self.expanded:
            self.Loc.x += self.speed

