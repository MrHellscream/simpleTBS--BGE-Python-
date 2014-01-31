#!/usr/bin/env python
""" generated source for module Mechanic """
# package: units
from units.Base import Base
class Mechanic(Base):
    """ generated source for class Mechanic """
    def __init__(self, owner, xx, yy, active):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy, active)
        self.name = "Mechanic"
        self.nick = "Mech"
        self.desc = "Slow infantry with some anti vehicle stuff."
        self.img = 1
        self.speed = 3
        self.cost = 200
        self.raider = True

