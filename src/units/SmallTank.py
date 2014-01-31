#!/usr/bin/env python
""" generated source for module SmallTank """
# package: units
from units.Base import Base
class SmallTank(Base):
    """ generated source for class SmallTank """
    def __init__(self, owner, xx, yy, active):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy, active)
        self.name = "Small Tank"
        self.nick = "STnk"
        self.desc = "A small tank, very effective against lightly armored opponents."
        self.legs = self.Move.TANK
        self.speed = 6
        self.img = 2

