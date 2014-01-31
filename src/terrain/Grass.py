#!/usr/bin/env python
""" generated source for module Grass """
# package: terrain
from terrain.Base import Base 
class Grass(Base):
    """ generated source for class Grass """
    def __init__(self):
        """ generated source for method __init__ """
        #super(Grass, self).__init__()
        self.name = "Grass"
        self.oldx = x = 1
        self.oldy = y = 0

    def speed(self):
        """ generated source for method speed """
        return 0.8

    def defense(self):
        """ generated source for method defense """
        return 0.9

