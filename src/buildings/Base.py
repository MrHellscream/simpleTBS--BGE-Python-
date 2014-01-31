#!/usr/bin/env python
""" generated source for module Base """
# package: buildings


class Base(object):
    import buildings 
    
    """ generated source for class Base """
    # Image and other info
    # (y*width+x) = id so when saving it can place it in the correct location.
    editorid = 0
    img = 0
    name = "Bacon"
    desc = "Giggles"
    Locked = bool()

    # Easy determination if a unit is standing on it or not. TODO: Install this or do something.
    Menu = ""

    # The menu this opens.
    class Units:
        """ generated source for enum Units """
        GROUND = "GROUND"
        AIR = "AIR"
        WATER = "WATER"

    unittype = Units.GROUND

    # Health (How long until it is captured / destroyed, and how far along it is)
    maxhealth = 20
    health = maxhealth

    # owner's ID and team #
    owner = int()
    team = 0

    # Location
    x = int()
    y = int()

    def __init__(self, owner, xx, yy):
        """ generated source for method __init__ """
        #print '1',self.buildings.GAME
        self.Game=self.buildings.GAME
        #print ('1',self.Game)
        # 15 = Neutral, 12~14 are unused. (12 max players)
        print ('%s'  % "Base level owner: " + str(owner))
        self.owner = owner
        self.x = xx
        self.y = yy
        self.editorid = self.y * self.Game.gameMap.width + self.x
        self.img = 0

    def OpenMenu(self):
        """ generated source for method OpenMenu """
        if self.Menu != None:
            menus.City(self.Menu, self.x, self.y)

    def Capture(self, hp, winner):
        """ generated source for method Capture """
        # TODO: Fix this up to work properly
        # TODO: Animation trigger for capturing.
        self.health -= hp
        if self.health <= 0:
            print ('%s'  % "Building Captured!")
            if self.name == "Capital":
                self.Game.btl.CaptureCapital(self.x, self.y)
            print ('%s'  % "Herp Derp")
            self.owner = winner
            self.team = self.Game.player[winner].team
            self.health = self.maxhealth
        else:
            print ( "Building hp :%s " % self.health)

    def DrawMe(self):
        """ generated source for method DrawMe """
        loc = [self.img, self.team]
        return loc

