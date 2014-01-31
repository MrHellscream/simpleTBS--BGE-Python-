#!/usr/bin/env python
""" generated source for module Terrain """
# package: gui

class Terrain(object):
    def Draw(self, Game, scene):
        print (' Game.gameMap.width %s' % Game.gameMap.width)
        print (' Game.gameMap.height %s' % Game.gameMap.height)
        i=0
        GameObjectInactive=scene.objectsInactive
        for x in range(Game.gameMap.height):
            for y in range(Game.gameMap.width):
                #xx = Game.gameMap.mapGame[x][y].x
                #yy = Game.gameMap.mapGame[x][y].y
                TerrainObject=Game.gameMap.mapGame[x][y]
                #print ('Game.gameMap.mapGame %s ' % TerrainObject,TerrainObject.name,x,y)   
                #print (' i %s' % i)
                
                #print ('Empty %s ' % scene.objects["Empty"])
                #scene.objects["Empty"].position=(-x*2-1.5,-y*2-1.5,0.9)
                scene.objects["Empty"].position=(-x-1.5,-y-1.5,0.9)
                #print ('Empty %s ' %scene.objects["Empty"].position)                
                scene.addObject(GameObjectInactive[TerrainObject.name], "Empty")
            

