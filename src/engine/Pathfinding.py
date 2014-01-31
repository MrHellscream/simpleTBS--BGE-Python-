#!/usr/bin/env python

# package: engine

# Future place of the A-star path finding algorithm
class Pathfinding(object):
    
    # The lists used for finding things.
    class PathNode(object):      
        cost = float()
        loc = []

        def __init__(self, x, y, cost): 
            self.loc = [x, y]
            self.cost = cost
            
    def __init__(self,Game):
        self.Game=Game
        self.openlist = []
        self.closedlist = []

        # Used for tracking the currently selected node and a shortcut to the currently selected unit.
        #self.unit = units.Base()
        #self.current = self.PathNode()
        self.distance = int()

        # Output information
        self.mapGame = []
        self.maphits = []

        # View Tile Cost/Hits and when the last time something was updated.
        self.ShowCost = bool()
        self.ShowHits = bool()
        self.LastChanged = 1
        
    def SwitchParentClosed(self, node):
        cost = self.Game.gamegameMap.mapGameGame[node.loc[0]][node.loc[1]].speed() + self.current.cost
        if cost < node.cost:
            node.cost = int(cost * 100.0) / 100.0
            self.closedlist.remove(node)
            self.openlist.append(node)
            
    def SwitchParent(self, node):
        cost = self.Game.gameMap.mapGame[node.loc[0]][node.loc[1]].speed() + self.current.cost
        if cost < node.cost:
            node.cost = int(cost * 100.0) / 100.0

    def SwitchParentClosed(self, node):
        """ generated source for method SwitchParentClosed """
        cost = self.Game.gameMap.mapGame[node.loc[0]][node.loc[1]].speed() + self.current.cost
        if cost < node.cost:
            node.cost = int(cost * 100.0) / 100.0
            self.closedlist.remove(node)
            self.openlist.append(node)

    def FindCost(self, x, y, parent):
        cost = self.Game.gameMap.mapGame[y][x].speed()
        if parent != None:
            cost += parent.cost
        return int(cost * 100.0) / 100.0

   

    def InOpen(self, x, y):

        for node in self.openlist:
            if node.loc[0] == x and node.loc[1] == y:
                self.SwitchParent(node)
                return True
        return False

    def InClosed(self, x, y):
        for node in self.closedlist:
            if node.loc[0] == x and node.loc[1] == y:
                self.SwitchParentClosed(node)
                return True
        return False
    def AddNode(self, x, y):
        if not self.InClosed(x, y):
            if not self.InOpen(x, y):
                cost = int(self.FindCost(x,y,self.current)*100.0) / 100.0
                if cost <= self.distance:
                    self.openlist.append(self.PathNode(x, y, cost))
                    
                    
    def SwitchParent(self, node):
        cost = self.Game.gameMap.mapGame[node.loc[1]][node.loc[0]].speed() + self.current.cost
        if cost < node.cost:
            node.cost = int(cost * 100.0) / 100.0

    def SwitchParentClosed(self, node):
        cost = self.Game.gameMap.mapGame[node.loc[1]][node.loc[0]].speed() + self.current.cost
        if cost < node.cost:
            node.cost = int(cost * 100.0) / 100.0
            self.closedlist.remove(node)
            self.openlist.append(node)

    def FindCost(self, x, y, parent):
        cost = self.Game.gameMap.mapGame[y][x].speed()
        if parent != None:
            cost += parent.cost
        return int(cost * 100.0) / 100.0

    def RemoveOccupied(self):
        if len(self.map) <= 1:
            return
        i = 1
        while i < len(self.map):
            if self.Occupied(self.map[i][0], self.map[i][1]):
                self.map.remove(i)
            i += 1

    def Occupied(self, x, y):
        for unit in self.Game.units:
            if self.unit.x == x and self.unit.y == y:
                return True
        return False

    def LowestCostOpen(self):
        if len(self.openlist)==0:
            return None
        lowest = self.openlist[0]
        for node in self.openlist:
            if node.cost > lowest.cost:
                lowest = node
        return lowest

    

    def FindNodes(self):
        if self.current.loc[0] - 1 >= 0 and self.unit.PathCheck(self.current.loc[0] - 1, self.current.loc[1]):
            self.AddNode(self.current.loc[0] - 1, self.current.loc[1])
        if self.current.loc[1] - 1 >= 0 and self.unit.PathCheck(self.current.loc[0], self.current.loc[1] - 1):
            self.AddNode(self.current.loc[0], self.current.loc[1] - 1)
        if self.current.loc[0] + 1 < self.Game.gameMap.width and self.unit.PathCheck(self.current.loc[0] + 1, self.current.loc[1]):
            self.AddNode(self.current.loc[0] + 1, self.current.loc[1])
        if self.current.loc[1] + 1 < self.Game.gameMap.height:
            if self.unit.PathCheck(self.current.loc[0], self.current.loc[1] + 1):
                self.AddNode(self.current.loc[0], self.current.loc[1] + 1)
                
    def FindPath(self, unit, _range):
        self.maphits = [ [0 for y in range(self.Game.gameMap.width)] for x in range(self.Game.gameMap.height)]
        self.openlist = []
        self.closedlist = []
        self.map = []
        self.distance = _range
        self.unit = unit
        self.openlist.append(self.PathNode(unit.x, unit.y, 0))
        print("self.openlist %s" %self.openlist[0].loc)
        self.current = self.openlist[0]
        #print("%s" %self.current)
        while True:
            if len(self.openlist)==0:
                break
            self.FindNodes()
            self.closedlist.append(self.current)
            self.openlist.remove(self.current)
            
            self.maphits[self.current.loc[1]][self.current.loc[0]] += 1
            self.current = self.LowestCostOpen()
        for node in self.closedlist:
            self.map.append((node.loc[0], node.loc[1]))
	    #print("%s" % self.map)
        #unit.LastPathed = System.currentTimeMillis()
        self.RemoveOccupied()
        return self.map
