#!/usr/bin/env python
""" generated source for module Selector """
# package: gui

# 
#  * This draws 4 different images (each corner) of the selector and moves them in/out in connection with the current frame (at 1/2 speed) [Based off 12 max]
#  * @param g = The Graphics2D to drawn too.
#  * @param resize = Size setup of the window to use.
#  * @author SergeDavid
#  * @version 0.5
#  
class Selector(object):
    """ generated source for class Selector """
    Dev = False

    @classmethod
    def Draw(cls, frame_, g, resize, x, y):
        """ generated source for method Draw """
        size = int(Math.pow(2, Game.load.Times_Extras))
        if Game.view.Viewable(x, y):
            x -= Game.view.ViewX()
            y -= Game.view.ViewY()
            off += 2
            if cls.Dev == True:
                ShowArea(g, x, y, resize, off)
            g.drawImage(Game.img_exts, x * resize - off, y * resize - off, x * resize + (resize / 2) - off, y * resize + (resize / 2) - off, size * 3, size * 3, size * 3 + (size / 2), size * 3 + (size / 2), None)
            g.drawImage(Game.img_exts, x * resize + (resize / 2) + off, y * resize - off, x * resize + resize + off, y * resize + (resize / 2) - off, size * 3 + (size / 2), size * 3, size * 3 + size, size * 3 + (size / 2), None)
            g.drawImage(Game.img_exts, x * resize - off, y * resize + (resize / 2) + off, x * resize + (resize / 2) - off, y * resize + resize + off, size * 3, size * 3 + (size / 2), size * 3 + (size / 2), size * 3 + size, None)
            g.drawImage(Game.img_exts, x * resize + (resize / 2) + off, y * resize + (resize / 2) + off, x * resize + resize + off, y * resize + resize + off, size * 3 + (size / 2), size * 3 + (size / 2), size * 3 + size, size * 3 + size, None)

    @classmethod
    def ShowArea(cls, gg, x, y, size, off):
        """ generated source for method ShowArea """
        gg.drawRect(x * size - off, y * size - off, size / 2, size / 2)
        gg.drawRect(x * size + (size / 2) + off, y * size - off, size / 2, size / 2)
        gg.drawRect(x * size - off, y * size + (size / 2) + off, size / 2, size / 2)
        gg.drawRect(x * size + (size / 2) + off, y * size + (size / 2) + off, size / 2, size / 2)

