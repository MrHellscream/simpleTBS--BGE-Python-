#!/usr/bin/env python
""" generated source for module Shipyard """
# package: buildings
# import engine.Game;
from buildings.Base import Base
class Shipyard(Base):
    """ generated source for class Shipyard """
    def __init__(self, owner, xx, yy):
        """ generated source for method __init__ """
        Base.__init__(self,owner, xx, yy)
        self.name = "Capital"
        self.desc = "Creates water units."
        self.img = 4
        self.Menu = "shipyard"
        # Game.map.map[yy][xx].swim = true;

