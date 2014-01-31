#!/usr/bin/env python
""" generated source for module Airport """
# package: buildings
from buildings.Base import Base
class Airport(Base):
    """ generated source for class Airport """
    def __init__(self, owner, xx, yy):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy)
        self.name = "Airport"
        self.desc = "Creates Air units."
        self.img = 3
        self.Menu = "airport"

