#!/usr/bin/env python
""" generated source for module Base """
# package: unitsim
import time
class Base(object):
    import units
    """ generated source for class Base """
    name = "Missing No."
    nick = "MsNo"
    desc = "Unknown description present."
    owner = int()
    img = int()
    UModels="None"
    # Extras
    Fog = 5

    # Fog of war setting.
    cost = 100
    building = "barracks"

    # Which building it can be bought from.
    raider = False
    bld = -1

    # The building this unit is currently standing on, null or -1 if none.
    MaxFuel = 1000
    Fuel = 1000

    # Total fuel left
    Ammo = 10

    # Ammo used for the main weapon, secondary weapon doesn't run out.
    # life settings
    dead = bool()
    maxhp = 100
    health = maxhp
    moved = bool()
    acted = bool()

    # Pathing Stuff
    Map = []

    # TEST
    LastPathed = 0

    # Location
    x = int()
    y = int()
    oldx = int()
    oldy = int()
    speed = 2

    # This is the movement type of the unit. 0 = Infantry, 1 = Vehicle, 2 = Tank, 3 = Ship, 4 = Aircraft
    class Move:
        """ generated source for enum Move """
        INF = "INF"
        TIRE = "TIRE"
        TANK = "TANK"
        SHIP = "SHIP"
        FLY = "FLY"

    legs = Move.INF

    # Battle Settings 
    # TODO: Add alternate weapon setup
    MoveAndShoot = True

    # Allows units to move then shoot, or make them stay in the same location in order to attack.
    MaxAtkRange = 1

    # How many squares away from the unit can it attack. (1 being default, 0 being none)
    MinAtkRange = 1

    # This is used for ranged units such as artillery.
    MainAttack = [55, 50, 10, 20, 20, 50, 50, 50, 50]

    # Extra (For mods)
    # What can and can't be shot at.
    class Armor:
        """ generated source for enum Armor """
        FOOT = "FOOT"
        VEHICLE = "VEHICLE"
        TANK = "TANK"
        AIR = "AIR"
        SHIP = "SHIP"
        ALL = "ALL"
        NONE = "NONE"

    # TODO: Hook this up to attacking.
    ArmorType = Armor.FOOT
    MainATK = [Armor.ALL]

    # The main attack to be used.
    #  I need to add what kind of unit is being constructed or split it into extended classes.
    # 	 * 
    # 	 * @param owner = What player owns this unit.
    # 	 * @param xx = The X location of the unit.
    # 	 * @param yy = The Y location of the unit.
    #
    def CityPointer(self):
        """ generated source for method CityPointer """
        if self.bld != -1:
            if self.oldx != self.x or self.oldy != self.y:
                self.Game.builds[self.bld].health = self.Game.builds[self.bld].maxhealth
            self.Game.builds[self.bld].Locked = False
        self.bld = -1
        i = 0
        while i < len(self.Game.builds):
            if self.Game.builds[i].x == self.x and self.Game.builds[i].y == self.y:
                self.bld = i
                self.Game.builds[self.bld].Locked = True
                return
            i += 1
            
    def __init__(self, owner, xx, yy, active):
        """ generated source for method __init__ """
        self.Game=self.units.GAME
        self.owner = owner
        self.oldx = self.x = xx
        # Old locations are used when someone changes their minds on moving a unit.
        self.oldy = self.y = yy
        self.CityPointer()
        if not active:
            # On building option.
            self.acted = True
            self.moved = True
           ## self.Game.pathing.LastChanged = time.time()

    # This is currently being used by the path finding, the other is so I can have a pretty visual for actually moving it.
    def PathCheck(self, destx, desty):
        """ generated source for method PathCheck """
        if destx < 0 or desty < 0:
            return False
        if destx >= self.Game.gameMap.width or desty >= self.Game.gameMap.height:
            return False
        for unit in self.Game.units:
            # Allows units in the same team to walk past each other.
            if unit.x == destx and unit.y == desty and self.Game.player[unit.owner].team != self.Game.player[self.owner].team:
                return False
        if self.legs==self.Move.INF:
            if self.Game.gameMap.mapGame[desty][destx].walk:
                return True
        elif self.legs==self.Move.TIRE:
            if self.Game.gameMap.mapGame[desty][destx].drive:
                return True
        elif self.legs==self.Move.TANK:
            if self.Game.gameMap.mapGame[desty][destx].drive:
                return True
        elif self.legs==self.Move.SHIP:
            if self.Game.gameMap.mapGame[desty][destx].swim:
                return True
        elif self.legs==self.Move.FLY:
            if self.Game.gameMap.mapGame[desty][destx].fly:
                return True
        else:
            if self.Game.gameMap.mapGame[desty][destx].fly:
                return True
        return False

    def inrange(self, xx, yy):
        """ generated source for method inrange """
        xx = xx - self.x if (xx > self.x) else self.x - xx
        yy = yy - self.y if (yy > self.y) else self.y - yy
        if xx + yy > self.MaxAtkRange:
            return False
        if xx + yy < self.MinAtkRange:
            return False
        return True

    def attack(self, destx, desty, returnfire):
        """ generated source for method attack """
        if (self.x != self.oldx and self.y != self.oldy) and not self.MoveAndShoot:
            return False
        target = self.FindTarget(destx, desty, True, False)
        if target != None:
            if self.inrange(target.x, target.y):

                target.health -= damage
                if target.health <= 0:
                    damage += target.health
                    if target.bld != -1:
                        Game.builds[target.bld].Locked = False
                    self.Game.units.remove(target)
                    self.Game.player[self.owner].kills += 1
                    self.Game.player[target.owner].loses += 1

                elif returnfire:
                    target.attack(self.x, self.y, False)
                self.Game.player[self.owner].Powerup(damage, False)
                self.Game.player[target.owner].Powerup(damage, True)
                return True
        return False
 
    def capture(self, destx, desty):
        """ generated source for method capture """
        if not self.raider:
            return
        if destx == self.x and desty == self.y:
            if self.bld != -1:
                city = self.Game.builds[self.bld]
                if city.team != self.Game.player[self.owner].team:
                    city.Capture(int((self.health / 10 * self.Game.player[self.owner].CaptureBonus)), self.owner)

    
    def action(self, destx, desty):
        """ generated source for method action """
        if self.acted:
            return
        if not self.attack(destx, desty, True):
            self.capture(destx, desty)
        self.acted = True        
    



    def cancle(self):
        """ generated source for method cancle """
        if self.moved and not self.acted:
            self.moved = False
            self.x = self.oldx
            self.y = self.oldy

    def Pathing(self):
        """ generated source for method Pathing """
		
        if self.LastPathed < self.Game.pathing.LastChanged:
            distance = self.Fuel if (self.Fuel < self.speed) else self.speed
            self.map = self.Game.pathing.FindPath(self, distance)
            print("%s" % self.map)		

    def DrawMe(self):
        """ generated source for method DrawMe """
        loc = [self.img, self.owner * 2]
        if self.acted:
            loc[1] += 1
        return loc

    

    def FindTarget(self, destx, desty, hostilefire, friendlyfire):
        """ generated source for method FindTarget """
        for unit in self.Game.units:
            if self.Game.player[unit.owner].team != self.Game.player[self.owner].team or friendlyfire:
                if unit.x == destx and unit.y == desty:
                    return unit
        return None

    def FuelCost(self, x2, y2):
        """ generated source for method FuelCost """
        used = self.x - x2 if (self.x > x2) else x2 - self.x
        used += self.y - y2 if (self.y > y2) else y2 - self.y
        return used

    def DamageFormula(self, target):
        """ generated source for method DamageFormula """
        dmg = self.MainAttack[FindUnitID(target)]
        dmg *= self.health * 0.01
        dmg *= self.Game.player[self.owner].WeaponBonus
        dmg -= (target.health * 0.01) * self.Game.player.get(target.owner).ArmorBonus
        dmg -= (target.health * 0.01) * self.Game.gameMap.mapGame[target.y][target.x].defense()
        if dmg < 0:
            dmg = 0
        return dmg

    def FindUnitID(self, target):
        """ generated source for method FindUnitID """
        i = 0
        while i < len(self.Game.displayU):
            if self.Game.displayU[i].name == target.name:
                return i
            i += 1
        return 0

    def moveable(self, destx, desty):
        """ generated source for method moveable """
        if destx < 0 or desty < 0:
            return False
        if destx >= self.Game.gameMap.width or desty >= self.Game.gameMap.height:
            return False
        if self.Pathed(destx, desty):
            return True
        return False

    def Pathed(self, destx, desty):
        """ generated source for method Pathed """
        for p in self.map:
            if p[0] == destx and p[1] == desty:
                return True
        return False

    def Medic(self):
        """ generated source for method Medic """
        if self.Game.builds[self.bld].team != Game.player[self.owner].team:
            return
        hp = self.health + 20
        if hp > self.maxhp:
            hp = self.maxhp
        money = Math.floor((hp - self.health) * 5)
        if money <= self.Game.player[Game.btl.currentplayer].money:
            self.Game.player[Game.btl.currentplayer].money -= money
            self.health = hp
            self.Fuel = self.MaxFuel
            
    def move(self, destx, desty):
        """ generated source for method move """
        if self.moved:
            return
        if self.moveable(destx, desty):
            print ('move %s '  % self )
            print ('------------------------------>> %s %s' % (destx, desty))
            self.Fuel -= self.FuelCost(destx, desty)
            self.moved = True
            self.oldx = self.x
            self.oldy = self.y
            self.x = destx
            self.y = desty
            self.UModels.position=(-self.y-1.5,-self.x-1.5,1)
            self.CityPointer()
            #self.Game.pathing.LastChanged = System.currentTimeMillis()
