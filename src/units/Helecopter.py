#!/usr/bin/env python
""" generated source for module Helecopter """
# package: units
from units.Base import Base
class Helecopter(Base):
    """ generated source for class Helecopter """
    def __init__(self, owner, xx, yy, active):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy, active)
        self.name = "Helecopter"
        self.nick = "Hele"
        self.desc = "A fast reaction unit that kills things."
        self.img = 4
        self.speed = 8
        self.legs = self.Move.FLY
        self.ArmorType = self.Armor.AIR
        self.building = "airport"

