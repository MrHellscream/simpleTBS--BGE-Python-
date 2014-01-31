#!/usr/bin/env python
""" generated source for module Water """
# package: terrain
from terrain.Base import Base 
class Water(Base):
    """ generated source for class Water """
    def __init__(self):
        """ generated source for method __init__ """
        #super(Water, self).__init__()
        self.name = "Water"
        self.oldx = x = 1
        self.oldy = y = 2
        self.MultiTiled = True
        self.walk = False
        self.drive = False
        self.swim = True

    def speed(self):
        """ generated source for method speed """
        return 1

    def defense(self):
        """ generated source for method defense """
        return 1

