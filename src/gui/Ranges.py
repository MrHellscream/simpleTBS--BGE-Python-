#!/usr/bin/env python
""" generated source for module Ranges """
# package: gui
#import java.awt.Color

#import java.awt.Graphics2D

#import java.awt.Point

#import units.Base

#import engine.Game

#import engine.Pathfinding

# 
#  * Depending on if a unit is selected by the current player and the units state, it will draw the movement range (based on path finding outcome).
#  * with the inclusion of two development settings to display times a tile has been hit in path finding, or just the tiles cost.
#  * It will also draw the attackable locations depending on the units max and min attack ranges.
#  * @author SergeDavid
#  * @version 0.3
#  
class Ranges(object):
    """ generated source for class Ranges """
    @classmethod
    def Draw(cls, gg, resize):
        """ generated source for method Draw """
        if Game.player.get(Game.btl.currentplayer).unitselected:
            if unit.moved and not unit.acted:
                Attacking(gg, unit, size, resize)
            elif not unit.moved:
                Moving(gg, unit, size, resize)
                gg.setColor(Color(255, 255, 255))
                if Game.pathing.ShowCost:
                    ShowCost(gg, resize)
                if Game.pathing.ShowHits:
                    ShowHits(gg, resize)

    @classmethod
    def Attacking(cls, gg, unit, size, resize):
        """ generated source for method Attacking """
        # If the unit disabled MoveAndShoot, then it won't display it's attack range since it can't attack.
        if unit.x != unit.oldx and unit.y != unit.oldy and not unit.MoveAndShoot:
            return
        # TODO: Maybe change this into a list of points like moving instead of playing with a block.
        y = unit.y - unit.MaxAtkRange
        while y <= unit.y + unit.MaxAtkRange:
            while x <= unit.x + unit.MaxAtkRange:
                if Game.view.Viewable(x, y):
                    if unit.inrange(x, y):
                        gg.drawImage(Game.img_exts, (x - Game.view.ViewX()) * resize, (y - Game.view.ViewY()) * resize, (x - Game.view.ViewX()) * resize + resize, (y - Game.view.ViewY()) * resize + resize, 0, 0, size, size, None)
                x += 1
            y += 1

    @classmethod
    def Moving(cls, gg, unit, size, resize):
        """ generated source for method Moving """
        for p in unit.map:
            if Game.view.Viewable(p.x, p.y):
                gg.drawImage(Game.img_exts, (p.x - Game.view.ViewX()) * resize, (p.y - Game.view.ViewY()) * resize, (p.x - Game.view.ViewX()) * resize + resize, (p.y - Game.view.ViewY()) * resize + resize, 0, size, size, size * 2, None)

    @classmethod
    def ShowCost(cls, gg, size):
        """ generated source for method ShowCost """
        for node in Game.pathing.closedlist:
            if Game.view.Viewable(node.loc.x, node.loc.y):
                gg.drawString(node.cost + "", (node.loc.x - Game.view.ViewX()) * size + size / 4, (node.loc.y - Game.view.ViewY()) * size + size / 2)

    @classmethod
    def ShowHits(cls, gg, size):
        """ generated source for method ShowHits """
        y = 0
        while y < Game.map.height:
            while x < Game.map.width:
                if Game.view.Viewable(x, y):
                    gg.drawString(Game.pathing.maphits[y][x] + "", (x - Game.view.ViewX()) * size + size / 4, (y - Game.view.ViewY()) * size + size / 2)
                x += 1
            y += 1

