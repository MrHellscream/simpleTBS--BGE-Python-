#!/usr/bin/env python
""" generated source for module Artillery """
# package: units
from units.Base import Base
class Artillery(Base):
    """ generated source for class Artillery """
    def __init__(self, owner, xx, yy, active):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy, active)
        self.name = "Artillery"
        self.nick = "Art"
        self.desc = "A ranged unit."
        self.MoveAndShoot = False
        self.legs = self.Move.TIRE
        self.img = 3
        self.speed = 4
        self.MinAtkRange = 2
        self.MaxAtkRange = 4
        self.MainAttack = [0,100,100,100,100,100,100,100]

