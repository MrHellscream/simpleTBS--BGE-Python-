#!/usr/bin/env python
""" generated source for module Barracks """
# package: buildings
from buildings.Base import Base
class Barracks(Base):
    """ generated source for class Barracks """
    def __init__(self, owner, xx, yy):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy)
        self.name = "Barracks"
        self.desc = "Creates ground units."
        self.img = 2
        self.Menu = "barracks"

