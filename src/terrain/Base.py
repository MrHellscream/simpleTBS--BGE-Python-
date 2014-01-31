#!/usr/bin/env python
""" generated source for module Base """
# package: terrain
class Base(object):
    """ generated source for class Base """
    x = 0
    y = 0
    name = "Void"
    walk = True
    drive = True
    swim = False
    fly = True
    oldx = x

    # Used for editor stuff
    oldy = y
    MultiTiled = False

    # Determines if ChangeTiles is called or not because the tile has multiple settings.
    def building(self):
        """ generated source for method building """
        return False

    def speed(self):
        """ generated source for method speed """
        return 1

    # Path Cost based on 10 (-10 = almost none, +10 = a ton)
    def defense(self):
        """ generated source for method defense """
        return 1

    # Protection offered for those being shot at.

