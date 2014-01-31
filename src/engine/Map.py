#!/usr/bin/env python
""" generated source for module Map """
# package: engine
import terrain
from engine.MapParser import MapParser 
class Map(object):
    import terrain
    """ generated source for class Map """
    # Base settings
    width = 12
    height = 12
    minsize = 6
    maxsize = 64
    auther = str()
    desc = str()
    
    # A square/rectangular area that you play on. Diamond shaped if isometric.
    mapGame = []
    tiles = []
    
    parse = MapParser

    def __init__(self,Game):
        """ generated source for method __init__ """
        self.Parser=MapParser(Game)
        self.terrain.GAME=Game
    def MapSetup(self, width, height):
        a=1
        """ generated source for method MapSetup """
        if (width<self.minsize): width=self.minsize
        if (width>self.maxsize): width=self.maxsize
        if (height<self.minsize): height=self.minsize
        if (height>self.maxsize): height=self.maxsize
        self.width=width
        self.height=height
        #print self.width,self.height
        #map = new terrain.Base[height][width];
        #TODO: Current way of keeping the map clean, I should find a way of doing this with a smaller startup cost.
        self.mapGame=[ [0 for y in range(width)] for x in range(height)]
				
	
    def  getTile(self, i):
        terrain_array={0 : self.terrain.Dirt,
           1 : self.terrain.Forest,
           2 : self.terrain.Mountain,
           3 : self.terrain.Water,
           4 : self.terrain.City,
           5 : self.terrain.Road,
                 }
        return terrain_array[i]()
            
