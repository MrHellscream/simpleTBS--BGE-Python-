#!/usr/bin/env python
""" generated source for module MapParser """
# package: engine
import sys,os
#from Game import BegGame
# encodes and decodes mapfiles. 
#  * The encoder is used solely by the map editor, (save is used to save battles)
#  * while the decode is used to load a map for the editor and battles via battle.newgame()
#  * @author SergeDavid
#  * @version 0.2
#

class MapParser():    
    """ generated source for class MapParser """
    adr=__file__
    ind=adr.rfind ("\\")
    nadr=adr[:ind+1]
    path =nadr+"maps"
    terrain = 0
    
    # Keeps track of current row
    # Handles building construction after the decoding loop is finished.
    CityString = str()
    CityPoint = []
    def __init__(self,Game, width = 58, height = 58):
        self.width = width
        self.height = height
        self.Game=Game
        
    def encode(self, mapname):
        """ generated source for method encode """
        # If the folder doesn't exist, create it so we can save our save files inside it.
        directory = File(self.path)
        if not directory.exists():
            if directory.mkdir():
                Game.error.ShowError("The " + self.path + " directory has been created.")
            else:
                Game.error.ShowError("Cannot create the maps directory. " + self.path + "")
                return
        # Saves the game in a property file (since it is easy)
        try:
            out.write(encodeInfo() + encodeDesc() + encodeCities() + encodeTerrain() + encodeUnits())
            out.close()
        except Exception as e:
            Game.error.ShowError("The map failed to save:" + e.getMessage())

    def encodeInfo(self):
        """ generated source for method encodeInfo """
        # TODO: Total players. (start with 2, and add more depending on unit and building owners.)
        w = Integer.toHexString(Game.map.width - 1)
        if 1 <= len(w):
            w = "0" + w
        h = Integer.toHexString(Game.map.height - 1)
        if 1 <= len(h):
            h = "0" + h
        return "1 " + w + h + "2"

    # Adds the current player's name with a description of the map to the map file separated by the first space
    def encodeDesc(self):
        """ generated source for method encodeDesc """
        # TODO: Replace name with current players name, and leave description for manliness?
        return "\n2 " + "PlayerName" + " " + "Description of Map"

    # Turns the building list into a string. (and sorts them into proper order)
    def encodeCities(self):
        """ generated source for method encodeCities """
        cities = ""
        Game.builds = FormatCities(Game.builds)
        if not Game.builds.isEmpty():
            cities += "\n3 "
            for bld in Game.builds:
                cities += Integer.toHexString(bld.owner)
                cities += CityID(bld)
        return cities

    # Turns the map into a series of strings.
    def encodeTerrain(self):
        """ generated source for method encodeTerrain """
        tiles = ""
        y = 0
        while y < Game.map.height:
            tiles += "\n4 "
            while x < Game.map.width:
                tiles += TerrainID(x, y)
                x += 1
            y += 1
        return tiles

    # Turns the unit list into a string.
    def encodeUnits(self):
        """ generated source for method encodeUnits """
        units = ""
        if not Game.units.isEmpty():
            units += "\n5 "
            for unit in Game.units:
                units += UnitID(unit)
                units += Integer.toHexString(unit.owner)
                if 1 <= len(x):
                    x = "0" + x
                if 1 <= len(y):
                    y = "0" + y
                units += x
                units += y
        return units

    def CityID(self, bld):
        """ generated source for method CityID """
        a = "00"
        i = 0
        while i < len(Game.displayB):
            if bld.name == Game.displayB.get(i.name):
                a = Integer.toHexString(i)
                break
            i += 1
        if 1 <= len(a):
            a = "0" + a
        return a

    def UnitID(self, unit):
        """ generated source for method UnitID """
        a = "00"
        i = 0
        while i < len(Game.displayU):
            if unit.name == Game.displayU.get(i.name):
                a = Integer.toHexString(i)
                break
            i += 1
        if 1 <= len(a):
            a = "0" + a
        return a

    def TerrainID(self, x, y):
        """ generated source for method TerrainID """
        i = 0
        while i < len(Game.map.tiles):
            if Game.map.map[y][x].name == Game.map.tiles.get(i.name):
                return Integer.toHexString(i)
            i += 1
        return "0"

    def FormatCities(self, oldblds):
        """ generated source for method FormatCities """
        newblds = ArrayList()
        while not oldblds.isEmpty():
            while i < len(oldblds):
                if oldblds.get(i).editorid < lowid:
                    lowest = i
                    lowid = oldblds.get(i).editorid
                i += 1
            newblds.add(oldblds.get(lowest))
            oldblds.remove(lowest)
        ##print "Begin Debugging!!!"
        i = 0
        while i < len(newblds):
            #print "id : " + i + " with an editorid : " + newblds.get(i).editorid
            i += 1
        return newblds

    
            
            
            
    def ParseInfo(self, info):
        """ generated source for method ParseInfo """
        if len(info)!=5:
            print ("%s" % "Map info is corrupt.")
            #Game.error.ShowError("Map info is corrupt.")
            return
        self.Game.gameMap.MapSetup(int(info[0: 2],16) + 1, int(info[2: 4],16)  + 1)
        self.Game.btl.MaxUsers(int(info[4: 5],16))

    def ParseDesc(self, info):
        """ generated source for method ParseDesc """
        self.auther = info[0]
        if len(info):
            self.desc = info[1]

    def ParseTerrain(self, info):
        """ generated source for method ParseTerrain """
        if self.Game.gameMap.width != len(info):
            print ("%s" % 'Game.error.ShowError(Terrain at row  (Too Long\Too Short))' )   
        if self.terrain >= self.height:
            return
        total = len(info)
     
        i = 0
        while i < total and i < self.width:
            using = int(info[i:i+1],16)
         
            self.Game.gameMap.mapGame[self.terrain][i] = self.Game.gameMap.getTile(using)
            if self.Game.gameMap.mapGame[self.terrain][i].building():
                self.CityPoint.append((i, self.terrain))
            i += 1
        self.terrain += 1

    def ParseBuilding(self, info, x, y):
        """ generated source for method ParseBuilding """
        #print ("%s Building" % info)
        self.Game.builds.append(self.Game.list_.CreateCity(int(info[0: 1],16), x, y, int(info[1:3],16)))

    def ParseUnit(self, info):
        """ generated source for method ParseUnit """
        #print ("%s Unit " % info)
        if 7 < len(info):
            return
        self.Game.units.append(self.Game.list_.CreateUnit(int(info[5: 7],16), int(info[0: 1],16), int(info[1: 3],16), int(info[3: 5],16), True))

    def decode(self, mapname):
        """ generated source for method decode """
        self.terrain = 0
        self.CityString = ""
        self.CityPoint = []
        
        
        print ("%s" % self.path + "\\" + mapname + ".txt")
        inMap = open(self.path + "\\" + mapname + ".txt",'r')
        
        
        ParseFunc=[self.ParseInfo,self.ParseDesc,self.ParseTerrain,self.ParseUnit]
        try:
            line = inMap.readline() 
            while (line):
                print ("%s" % line)
                lineParse=line[:1]
                info = line[2:].rstrip()
                if lineParse=='1':
                    self.ParseInfo(info)
                elif lineParse==("2"):
                    self.ParseDesc(info.split(' ',1))
                elif lineParse==("3"):
                    self.CityString += info
                elif lineParse==("4"):
                    self.ParseTerrain(info)
                elif lineParse==("5"):
                    self.ParseUnit(info)
                line = inMap.readline()

            #print ("%s" % self.terrain)
            #print ("%s" % self.height)
            if self.terrain < self.height:
                print("%s" % 'Game.error.ShowError("Terrain is corrupt, short " + (Game.map.height - self.terrain) + " rows.")')
            
            for p in self.CityPoint:
                if len(self.CityString)>= 3:   
                    self.ParseBuilding(self.CityString[0:3], p[0], p[1])
                    self.CityString = self.CityString[3:]
            ##Game.map.SwitchTiles()
            inMap.close()        
            return True
        except OSError:
            prin ("%s" %  "Map not found.")
            #Game.error.ShowError("Map not found.")
            inMap.close()
            return False
        
##if __name__ == '__main__':
##    import sys
##    a=MapParser()
##    a.decode('FourCorners')
