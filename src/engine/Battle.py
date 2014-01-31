#!/usr/bin/env python
""" generated source for module Battle """
# package: engine


# Put the game stuff in here so all I have to do is end/start this to make a game work or not.
class Battle(object):
    """ generated source for class Battle """
    # A count of all the players in the game, used before Game.player is populated so this is required.
    totalplayers = 2

    # The current player who is playing, this loops back to 0 when it goes too high.
    currentplayer = 0
    mapname = str()
    GameOver = bool()

    # Game settings
    FogOfWar = bool()
    startingmoney = 100

    # How much you start with each round.
    buildingmoney = 50

    # How much each building provides.
    day = 1

    # Winning condition settings
    playersleft = 1
    def __init__(self,Game):
        self.Game=Game
    def NewGame(self, mapname):
        """ generated source for method NewGame """
        self.Game.player = []
        self.Game.builds = []
        self.Game.units = []
        self.Game.view.Loc[0] = 0
        self.Game.view.Loc[1] = 0
        if not self.Game.gameMap.Parser.decode(mapname):
            self.Game.GameState = self.Game.State.MENU
            return
        self.mapname = mapname
        self.playersleft = self.totalplayers
        self.GameOver = False

        #         
    def Buildingcount(self, owner):
        """ generated source for method Buildingcount """
        total = 0
        for bld in self.Game.builds:
            if bld.owner == owner:
                total += 1
        return total
    
    def EndTurn(self):
        """ generated source for method EndTurn """
        ply = self.Game.player[self.currentplayer]
        for unit in self.Game.units:
            unit.acted = False
            unit.moved = False
        self.currentplayer += 1
        if self.currentplayer >= self.totalplayers:
            self.currentplayer = 0
            self.day += 1
        ply = self.Game.player[self.currentplayer]
        if self.day != 1:
            ply.money += self.buildingmoney * self.Buildingcount(self.currentplayer)
        for unit in self.Game.units:
            if unit.owner == self.currentplayer and unit.health < unit.maxhp and unit.bld != -1:
                unit.Medic()
        self.Game.pathing.LastChanged += 1

    # Grabs the number of buildings a player owns.
    

    def Action(self):
        """ generated source for method Action """
        ply = self.Game.player[self.currentplayer]
        if ply.npc:
            return
        if ply.unitselected:
            if self.currentplayer == self.Game.units[ply.selectedunit].owner:
                # Action
                if self.Game.units[ply.selectedunit].moved and not self.Game.units[ply.selectedunit].acted:
                    self.Game.units[ply.selectedunit].action(ply.selectx, ply.selecty)
                    ply.unitselected = False
                elif not self.Game.units[ply.selectedunit].moved:
                    # Move
                    self.Game.units[ply.selectedunit].move(ply.selectx, ply.selecty)
                else:
                    ply.unitselected = False
            else:
                ply.unitselected = False
        else:
            if not ply.FindUnit():
                ply.unitselected = False
                ply.FindCity()

    # This will be redone when I set up the unit buying menu.
    def Buyunit(self, type_, x, y):
        """ generated source for method Buyunit """
        cost = self.Game.displayU[type_].cost * self.Game.player[self.currentplayer].CostBonus
        if self.Game.player[self.currentplayer].money >= cost:
            self.Game.units.append(self.Game.list_.CreateUnit(type_, self.currentplayer, x, y, False))
            #self.Game.units[-1].name+= str(len(self.Game.units)-1)+ str(self.currentplayer)
            #print ('%s '  %self.Game.units[-1].name)
            UnitObject=self.Game.units[-1]
            self.Game.LoadUnits(UnitObject,x,y)
            self.Game.player[self.currentplayer].money -= cost

    def MaxUsers(self, Max):
        """ generated source for method MaxUsers """
        # HACK: Change when I add more images to support more players.
        self.totalplayers = Max
        print ('%s '  %"The game currently supports only 4 players, not " )

    def AddCommanders(self, coms, npc, start, city):
        """ generated source for method AddCommanders """
        self.startingmoney = start
        self.buildingmoney = city
        i = 0
        while i < self.totalplayers:
            # TODO: Team setup needs to be added.
            self.Game.player.append(self.Game.list_.CreateCommander(coms[i], i + 1, start, npc[i]))           
            #print ('%s i'  % i)
            #print ('%s Game.player'  % self.Game.player)
            i += 1
        #print ('%s Game.player'  % self.Game.player)    
        for bld in self.Game.builds:
            if bld.owner != 15:
                bld.team = self.Game.player[bld.owner].team
                self.Game.player[bld.owner].builds.append(bld)

    def CaptureCapital(self, x, y):
        """ generated source for method CaptureCapital """
        loser = 0
        i = 0
        while i < len(self.Game.builds):
            if self.Game.builds[i].x == x and self.Game.builds[i].y == y:
                self.Game.player[self.Game.builds[i].owner].defeated = True
                # Makes a player lose.
                loser = self.Game.builds[i].owner
                print ('%s'  % "Grrr " + loser)
                self.Game.builds.remove(i)
                self.Game.builds.append(i, self.Game.list_.CreateCity(self.currentplayer, x, y, 1))
                self.playersleft -= 1
                if self.playersleft <= 1:
                    self.GameOver = True
                    menus.EndBattle()
                break
            i += 1
        i = 0
        while i < len(self.Game.units):
            if self.Game.units[i].owner == loser:
                print ('%s'  % "Remove " + self.Game.units[i].owner)
                self.Game.units.remove(i)
            i += 1
        # TODO: Change all buildings to be owned by the player. 

