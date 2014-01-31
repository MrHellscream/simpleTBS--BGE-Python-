#!/usr/bin/env python
""" generated source for module ListData """
# package: engine
# 
#  * When adding a new commander, building, or unit to the game, just add the class to the Create#### switch.
#  * Load#### creates a unit, commander, city and then sets its properties to match its state when you saved the game.
#  * For finding type when Loading, it takes the units name, and compares it to the Display# list (reference list).
#  * The reference lists will be automatically updated thanks to ListData() constructor.
#  * @author SergeDavid
#  * @version 0.2

class ListData(object):
    
    """ generated source for class ListData """
 
    import players
    import buildings
    import units
   
    # Starting ListData() will load all of the commanders, buildings, and units into reference lists (display#) for use in menu's.
    def __init__(self,Game):
        self.buildings.GAME=Game
        self.players.GAME=Game
        self.units.GAME=Game
        #print '2',self.buildings.GAME
        
        """ generated source for method __init__ """
        # These loop for a max of 100 items (shouldn't hit that high), a null return from Create###(); will end the loop.
        i = 0
        while i < 100:
            Game.displayC.append(self.CreateCommander(i, 0, 0, False))
            
            if Game.displayC[i] == None:
                Game.displayC.pop(i)
                break
            i += 1
        print ('%s Game.displayC'  %Game.displayC)
        i = 0
        while i < 100:
            Game.displayB.append(self.CreateCity(-1, 0, 0, i))
            if Game.displayB[i] == None:
                Game.displayB.pop(i)
                break
            i += 1
        print ('%s Game.displayB'  %Game.displayB    )
        i = 0
        while i < 100:
            Game.displayU.append(self.CreateUnit(i, 0, 0, 0, False))
            if Game.displayU[i] == None:
                Game.displayU.pop(i)
                break
            i += 1
        print ('%s Game.displayU'  %Game.displayU)
    # 
    # 	 * This loads a playable commander into the game for the reference and in use commanders. [Battle]
    # 	 * @param which = Which commander to add (list must match order of LoadLists)
    # 	 * @param team = Which team the commander is joined too (A,B,C,D,Etc.)
    # 	 * @param money = How much money the player starts with
    # 	 * @param npc = If true, this commander is not playable by the player (controlled by the computer)
    # 	 
    def CreateCommander(self, which, team, money, npc):
        """ generated source for method CreateCommander """
        if not which<4: return None
        plopt = {0 : self.players.Andy,
           1 : self.players.Colin,
           2 : self.players.Max,
           3 : self.players.Sammi,
                    }
        
        return plopt[which](npc, team, money)
    
       

    # 
    # 	 * This creates a building (town/barracks/seaport) [MapParser]
    # 	 * @param owner = The player that owns the building (-1 to skip formatting) (15 is neutral, 12~14 are unused (and more if I lower max players from 12))
    # 	 * @param xx
    # 	 * @param yy
    # 	 * @param type = The building to be created in question.
    # 	 * @returnIt should never return null except for the reference list [ListData();]
    # 	 * 
    # 	 * @exception WARNING: removed the filter for proper owner buildings.
    # 	 
    def CreateCity(self, owner, xx, yy, type_):
        """ generated source for method CreateCity """
        # 15 = Neutral, 12, 13, 14 are unused. (12 max players)
        # TODO: Warning: I removed the check to make sure each building is legal.
        if not type_<4: return None
        print ('%s'  %"List level owner: " + str(owner))
        plopt = {0 : self.buildings.Capital,
           1 : self.buildings.Town,
           2 : self.buildings.Barracks,
           3 : self.buildings.Airport,
           4 : self.buildings.Shipyard,
                    }
        return plopt[type_](owner, xx, yy)
       

    # 
    # 	 * This creates a unit from a city and for reference. [Battle]
    # 	 * @param type = The unit in question being loaded from the switch.
    # 	 * @param owner = The player that the unit is commanded by.
    # 	 * @param xx
    # 	 * @param yy
    # 	 * @param active
    # 	 * @return It should never return null except for the reference list [ListData();]
    # 	 
    def CreateUnit(self, type_, owner, xx, yy, active):
        """ generated source for method CreateUnit """
        if not type_<4: return None
        plopt = {0 : self.units.Infantry,
           1 : self.units.Mechanic,
           2 : self.units.SmallTank,
           3 : self.units.Artillery,
           4 : self.units.Helecopter,
                 }
        return plopt[type_](owner, xx, yy, active)
        

    # 
    # 	 * This method is for creating a commander from a saved file.
    # 	 * @param Name
    # 	 * @param Defeated
    # 	 * @param Team
    # 	 * @param Money
    # 	 * @param Kills
    # 	 * @param Loses
    # 	 * @param Power
    # 	 * @param Using
    # 	 * @param npc
    # 	 
    def LoadCommander(self, Name, Defeated, Team, Money, Kills, Loses, Power, Using, npc):
        """ generated source for method LoadCommander """
        i = 0
        while i < len(Game.displayC):
            if Game.displayC.get(i).name == Name:
                Game.player.add(self.CreateCommander(i, Team, Money, npc))
                ply.defeated = Defeated
                ply.kills = Kills
                ply.loses = Loses
                ply.power = Power
                # TODO: Add in currently using power to player class and here.
            i += 1

    # 
    # 	 * This adds / changes a city from a saved file.
    # 	 * @param Name
    # 	 * @param Owner
    # 	 * @param Health
    # 	 * @param id
    # 	 
    def LoadCity(self, Name, Owner, Health, id):
        """ generated source for method LoadCity """
        # If the building changed (capital to town as an example) it will switch it.
        if not Name == Game.builds.get(id.name):
            while i < len(Game.displayB):
                if Game.displayB.get(i).name == Name:
                    Game.builds.append(id, self.CreateCity(Owner, Game.builds.get(id).x, Game.builds.get(id).y, i))
                i += 1
        # Changes owner and health of building to match it's current standings
        bld = Game.builds.get(id)
        bld.owner = Owner
        bld.health = Health

    def LoadUnit(self, Name, Owner, Health, Ammo, Fuel, X, Y, Acted):
        """ generated source for method LoadUnit """
        i = 0
        while i < len(Game.displayU):
            if Game.displayU.get(i).name == Name:
                Game.units.append(self.CreateUnit(i, Owner, X, Y, Acted))
                unit.health = Health
                unit.Ammo = Ammo
                unit.Fuel = Fuel
            i += 1

