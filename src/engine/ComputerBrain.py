#!/usr/bin/env python

# package: engine

##
##import units.Base

class ComputerBrain(object):
    """ generated source for class ComputerBrain """
    building = []
    finished = True
    DoneUnits = bool()
    UnitCount = int()
    DoneCities = bool()
    CityCount = int()
    from random import randint 
    def __init__(self,Game):
        self.Game=Game

    # This method is hit every game loop for npcs and handles a single unit / city so it is less heavy on the game.
    def ThinkDamnYou(self, ply):
        """ generated source for method ThinkDamnYou """
        # TODO: Redesign it to allow the npc to grab if someone is in firing range faster and easier.
        if self.finished:
            self.finished = False
            self.DoneCities = self.DoneUnits = False
            self.UnitCount = self.CityCount = 0
            if ply.power >= ply.level2:
                ply.UsePower(False)
            elif ply.power >= ply.level1:
                ply.UsePower(True)
                
        self.NextUnit(self.Game.btl.currentplayer)
        self.NextCities(self.Game.btl.currentplayer)
        
        if not self.DoneUnits:
            unit = self.Game.units[self.UnitCount]
            self.UnitCount += 1
            if unit.owner == self.Game.btl.currentplayer:
                self.HandleUnit(unit)
                
        elif not self.DoneCities:
            bld = self.Game.player[self.Game.btl.currentplayer].builds[self.CityCount]
            print ('Next build %s '  % bld)
            self.CityCount += 1
            self.HandleBuilding(bld)
        else:
            self.finished = True
            self.Game.btl.EndTurn()

    # Grabs the next unit in line, if none are found sets DoneUnits to true.
    def NextUnit(self, me):
        """ generated source for method NextUnit """
        if self.DoneUnits:
            return
        i = self.UnitCount
        while i < len(self.Game.units):
            if self.Game.units[i].owner == me:
                self.UnitCount = i
                return
            i += 1
        self.DoneUnits = True

    # Grabs the next city in line, if none are found sets DoneCities to true.
    def NextCities(self, me):
        """ generated source for method NextCities """
        if self.DoneCities:
            return
        i = self.CityCount
        while i < len(self.Game.player[me].builds):
            if not self.Game.player[me].builds[i].Menu == "":
                self.CityCount = i
                return
            i += 1
        self.DoneCities = True

    def HandleBuilding(self, bld):
        """ generated source for method HandleBuilding """
        if not bld.Menu == "":
            if not bld.Locked:
                if self.randint(0,2) == 0 or self.Game.btl.day < 3:
                    self.Game.btl.Buyunit(self.randint(0,3), bld.x, bld.y)
                    self.Game.player[bld.owner].selectx = bld.x
                    self.Game.player[bld.owner].selecty = bld.y

    def BuildingInRange(self, unit):
        """ generated source for method BuildingInRange """
        i = 0
        while i < len(unit.map):
            for bld in self.Game.builds:
                if bld.owner != unit.owner:
                    if bld.x == unit.map[i][0] and bld.y == unit.map[i][1]:
                        self.building = unit.map[i]
                        return True
            i += 1
        return False
    
    def HandleUnit(self, unit):
        """ generated source for method HandleUnit """
        unit.Pathing()
        if unit.raider and unit.bld != -1:
            # Finds, moves, and captures a building if the unit can capture it.
            if self.Game.builds[unit.bld].owner != unit.owner:
                unit.action(unit.x, unit.y)
                self.Game.player[unit.owner].selectx = unit.x
                self.Game.player[unit.owner].selecty = unit.y
                return
        if unit.raider and self.BuildingInRange(unit):
            unit.move(self.building[0], self.building[1])
            unit.action(self.building[0], self.building[1])
            unit.acted = True
            self.Game.player[unit.owner].selectx = unit.x
            self.Game.player[unit.owner].selecty = unit.y
        else:
            if self.WannaHug(unit):
                # Attack anyone near you.
                unit.acted = True
                return
            elif len(unit.map) <= 1:
                # For when a unit can't move anywhere
                self.WannaHug(unit)
                unit.acted = True
                return
            i=len(unit.map)-1
            while i >= 0:
                # Randomly selects somewhere to run.
                if self.randint(0,5) == 0:
                    unit.move(unit.map[i][0], unit.map[i][1])
                    self.Game.player[unit.owner].selectx = unit.x
                    self.Game.player[unit.owner].selecty = unit.y
                    self.WannaHug(unit)
                    unit.acted = True
                    break
                i -= 1

    # Looks for any enemies in range at the units current location by attacking each location in the attackable locations.
    def WannaHug(self, unit):
        """ generated source for method WannaHug """
        y = unit.y - unit.MaxAtkRange
        while y <= unit.y + unit.MaxAtkRange:
            x = unit.x - unit.MaxAtkRange
            while x <= unit.x + unit.MaxAtkRange:
                if unit.attack(x, y, True):
                    return True
                x += 1
            y += 1
        #  TODO Auto-generated method stub
        return False

    # Finds a building in the unit's movement range.
   

