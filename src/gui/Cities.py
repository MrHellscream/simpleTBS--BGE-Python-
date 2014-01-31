#!/usr/bin/env python
""" generated source for module Cities """
# package: gui


# 
#  * This draws all of the cities currently in the game that are visible.
#  * @param g = The Graphics2D to drawn too.
#  * @param resize = Size setup of the window to use.
#  * @author SergeDavid
#  * @version 0.4
#  
class Cities(object):
    """ generated source for class Cities """
    @classmethod
    def Draw(cls, g, resize):
        """ generated source for method Draw """
        size = int(Math.pow(2, Game.load.Times_City))
        xoff = Game.view.ViewX()
        yoff = Game.view.ViewY()
        for bld in Game.builds:
            if Game.view.Viewable(bld.x, bld.y):
                g.drawImage(Game.img_city, (bld.x - xoff) * resize, (bld.y - yoff) * resize, (bld.x - xoff) * resize + resize, (bld.y - yoff) * resize + resize, loc[0] * size, loc[1] * size, loc[0] * size + size, loc[1] * size + size, None)

