#!/usr/bin/env python
""" generated source for module Infantry """
# package: units
from units.Base import Base
class Infantry(Base):
    """ generated source for class Infantry """
    def __init__(self, owner, xx, yy, active):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy, active)
        self.name = "Infantry"
        self.nick = "Inf"
        self.desc = "Weakest units here."
        self.img = 0
        self.speed = 4
        self.raider = True

