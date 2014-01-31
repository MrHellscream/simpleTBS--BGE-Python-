#!/usr/bin/env python
""" generated source for module Base """
# package: players


class Base(object):
    import players
    """ generated source for class Base """
    # Basic Info
    name = str()
    desc = str()
    team = int()
    money = int()
    npc = bool()
    defeated = bool()
    builds=[]
    units=[]
    # Modifiers (unit cost/damage/defense)
    # Percentage offset for how much a unit costs to build with 1.0 = 100% (0.5 = half / 2.0 = double)
    CostBonus = 1.0
    ArmorBonus = 1.0

    # Currently just an overall bonus, TODO: Add in specific bonuses (foot, vehicle, tank, artillery, etc.)
    WeaponBonus = 1.0
    CaptureBonus = 1.0

    # Special Power
    # The current power level, max is level2.
    power = int()

    # The amount of power points needed to achieve the first ability. Set to 0 for it to not exist
    level1 = int()

    # The amount of power points needed to achieve the second ability.
    level2 = int()

    # Unit selection and unit end game statistics (total kills / loses)
    unitselected = bool()

    # If the character has selected a unit or not. (using this instead of selectedunit=-1)
    selectedunit = 0

    # Which unit is currently selected to use.
    usedunits = int()

    # How many units does the player have left until turn ends. Currently unused.
    kills = int()
    loses = int()

    # Player's image in the sprite sheet and the current looking location.
    imgx = int()
    imgy = int()
    selectx = 2
    selecty = 2

    # 
    # 	 * @param ai = If true, this character is not controlled by the player.
    # 	 * @param color = What team the player is associated with.
    # 	 * @param bling = The amount of money the player starts with.
    # 	 
    def __init__(self, ai, color, bling):
        """ generated source for method __init__ """
        self.Game=self.players.GAME
        # TODO: Might include an actual color attribute, but for now that is the team.
        self.team = color
        self.npc = ai
        self.money = bling

    def Powerup(self, damage, defending):
        """ generated source for method Powerup """
        self.power += damage / 3 if (defending) else damage
        if self.power > self.level2:
            self.power = self.level2

    # TODO: Remove the UserPower thing if I can get the direct MyPower1/2 to work correctly this time.
    #  This method is used in place of directly calling MyPower1 or 2
    # 	 * I did it so I don't have to add the (enough power and not 0) checks along with removing the appropriate amount.
    # 	 * 
    # 	 * @param which = if (true) {level 1 power} else {level 2 power}
    # 	 
    def UsePower(self, which):
        """ generated source for method UsePower """
        if which:
            if self.power >= self.level1 and self.level1 != 0:
                self.power -= self.level1
                MyPower1()
        else:
            if self.power >= self.level2 and self.level2 != 0:
                self.power -= self.level2
                MyPower2()

    # The first special ability the player can use when the players power>level1. leave level1 at 0 to remove access to this ability.
    def MyPower1(self):
        """ generated source for method MyPower1 """

    # The second ability, I might have these point to something like Game.powers.QuickFix();
    def MyPower2(self):
        """ generated source for method MyPower2 """

    def Cancle(self):
        """ generated source for method Cancle """
        if self.unitselected:
            self.Game.units.get(self.selectedunit).cancle()
            self.unitselected = False

    def FindUnit(self):
        """ generated source for method FindUnit """
        i = 0
        while i < len(Game.units):
            if self.Game.units.get(i).x == self.selectx and self.Game.units.get(i).y == self.selecty:
                if not self.Game.units.get(i).moved:
                    self.Game.units.get(i).Pathing()
                self.selectedunit = i
                self.unitselected = True
                return True
            i += 1
        return False

    def FindCity(self):
        """ generated source for method FindCity """
        # Finds a city to use for menu pickings.
        for bld in self.Game.builds:
            if bld.x == self.selectx and bld.y == self.selecty and bld.owner == self.Game.btl.currentplayer:
                bld.OpenMenu()
                return True
        return False

    # Returns the image location of the sprite sheet where this unit is located.
    def DrawMe(self):
        """ generated source for method DrawMe """
        imgx = 0
        imgy = 0
        loc = [imgx, imgy]
        return loc

