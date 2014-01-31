#!/usr/bin/env python
""" generated source for module Mountain """
# package: terrain
from terrain.Base import Base 
class Mountain(Base):
    """ generated source for class Mountain """
    def __init__(self):
        """ generated source for method __init__ """
        #super(Mountain, self).__init__()
        self.name = "Mountain"
        self.oldx = x = 2
        self.oldy = y = 0
        self.drive = False

    def speed(self):
        """ generated source for method speed """
        return 1.2

    def defense(self):
        """ generated source for method defense """
        return 1.5

