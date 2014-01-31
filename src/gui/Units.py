#!/usr/bin/env python
""" generated source for module Units """
# package: gui


# 
#  * This will draw all of the currently visible units. 
#  * Units not owned by the current player are turned around. (Simple way of telling units with the same color apart)
#  * @param g = The Graphics2D to drawn too.
#  * @param resize = Size setup of the window to use.
#  * @author SergeDavid
#  * @version 0.5
#  
class Units(object):
    """ generated source for class Units """
    @classmethod
    def Draw(self, UnitObject, scene,x,y):      
        GameObjectInactive=scene.objectsInactive
        #UnitObject=Game.units[-1]
        print (' Units create: %s %s %d %d' % (UnitObject,UnitObject.name,x,y))
        #print ('%s scene'  % scene.objects)
        
        scene.objects["Empty"].position=(-y-1.5,-x-1.5,1)
        UnitObject.UModels=scene.addObject(GameObjectInactive[UnitObject.name], "Empty")
        #print (' name: %s' %type(scene.objects["Empty"]))
        
        UnitObject.UModels.color=(0.1,0.2,0.3,1)
        #UModels.color
        print (' name: %s' % scene.objectsInactive[UnitObject.name].name) #= scene.objectsInactive[UnitObject.name].name.replace(search, replacement)
        #scene.objectsInactive[UnitObject.name].name= scene.objectsInactive[UnitObject.name].name.replace(UnitObject.name, "uuuuuuuuuuuuuuuuuuuuu")
        print (' Units position: %s' % scene.objects["Empty"].position)
        print ('----------------------------------------------')
                #ActionInfo.DrawUnitHP(g, resize, chars.x, chars.y, chars.health / 10)

