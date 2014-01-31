#!/usr/bin/env python
""" generated source for module Game """
# package: engine


class Game(object):
    """ generated source for class Game """
    serialVersionUID = 1

    # Application Settings
    build = "0"
    version = "2"
    name = "Strategy Game"
    ScreenBase = 32

    # Bit size for the screen, 16 / 32 / 64 / 128
    dev = True

    # Is this a dev copy or not... useless? D:
    class State:
        """ generated source for enum State """
        STARTUP = "STARTUP"
        MENU = "MENU"
        PLAYING = "PLAYING"
        EDITOR = "EDITOR"

    GameState = State.STARTUP

    # Setup the quick access to all of the other class files.
    import time
    from engine.Map import Map
    from engine.ListData import ListData
    
##    gui = Gui()
##    load = LoadImages()
##    input = InputHandler()
##    edit = Editor()
    from engine.Battle import Battle
##    error = ErrorHandler()
    from engine.Pathfinding import Pathfinding
    #pathing = Pathfinding()
##    list_ = ListData()
##    save = Save()
    from engine.ComputerBrain import ComputerBrain
##    brain = ComputerBrain()
##    finder = FileFinder()
    from engine.ViewPoint import ViewPoint
##    view = ViewPoint()

    # Image handling settings are as follows
##    fps = int()
##    fpscount = int()
##    img_menu = [None]*5
    img_tile = []
##    img_char = Image()
##    img_plys = Image()
##    img_city = Image()
##    img_exts = Image()
##    readytopaint = bool()

    # This handles the different players and also is used to speed logic arrays (contains a list of all characters they own)
    player = []
    builds = []
    units = []

    # These are the lists that will hold commander, building, and unit data to use in the menu's
    displayC =[]
    displayB = []
    displayU = []
    
    models_of_units_in_Game = []
    def __init__(self):
        """ generated source for method __init__ """
        # Creates all the gui elements and sets them up
        #self.gui = Gui(self)
        #self.gui.setFocusable(True)
        #self.gui.requestFocusInWindow()
        # load images, initialize the map, and adds the input settings.
        #self.load = LoadImages()
        self.gameMap=self.Map(self)
        self.list_ =self.ListData(self)
        self.btl=self.Battle(self)
        self.pathing = self.Pathfinding(self)
        self.brain = self.ComputerBrain(self)
        #self.input = InputHandler()
        self.view = self.ViewPoint()
        self.lastCPSTime = 0
        # This has been moved down here so that when everything is done, it is shown.
        #self.gui.LoginScreen()
        #self.save.LoadSettings()
        print ('%s'  % self.player)
        print ('%s'  % self.builds)
        print ('%s'  % self.units)
        print ('%s'  % self.GameState)
        

    def GameLoop(self):
        
        """ generated source for method GameLoop """
        loop = True
        last = self.time.time()
        #while loop:
            # Used for logic stuff
        
        # FPS settings
        if self.time.time() - self.lastCPSTime > 1:
            self.lastCPSTime = self.time.time()
##                self.fpscount = self.fps
##                self.fps = 0
            #self.error.ErrorTicker()
            #setTitle(self.name + " v" + self.build + "." + self.version + " : FPS " + self.fpscount)
            if self.GameState == self.State.PLAYING:
                print ('%s'  % "PLAYING")
                if self.player[self.btl.currentplayer].npc and not self.btl.GameOver:
                    print ('%s'  % "PLAY_Comp")
                    print (' currentplayer %s'  % self.btl.currentplayer)
                    print (' self.player[currentplayer] %s'  % self.player[self.btl.currentplayer])
                    self.brain.ThinkDamnYou(self.player[self.btl.currentplayer])
                    print (' units %s'  % self.units)
                    #print (' units_displayU %s'  %self.displayU)
           # else:
##                self.fps += 1
            # Current Logic and frames per second location (capped at 20 I guess?)
##            if time.time() - lastCPSTime2 > 100:
##                lastCPSTime2 = time.time()
##                logics = 0
##                if self.GameState == self.State.PLAYING or self.GameState == self.State.EDITOR:
##                    self.view.MoveView()
##                # This controls the view-point on the map
##                if self.GameState == self.State.EDITOR:
##                    if self.edit.holding and self.edit.moved:
##                        self.edit.AssButton()
##                Game.gui.frame_ += 1
##                # This is controlling the current frame of animation.
##                if Game.gui.frame_ >= 12:
##                    Game.gui.frame_ = 0
##                self.gui.repaint()
##            else:
##                logics += 1
            # Paints the scene then sleeps for a bit.
    def LoadTerrain(self):
        import bge 
        import bpy
        import gui
        
        scene = bge.logic.getCurrentScene()
        cont = bge.logic.getCurrentController()
        own = cont.owner
        print ('%s scene'  % scene)
        print ('%s scene'  % scene.objects)
        print ('%s scene'  % scene.objectsInactive)    
        print ('%s cont'  % cont)
        print ('%s own'  % own )
        GameObjectInactive=scene.objectsInactive
##        self.img_tile=[GameObjectInactive['Water'],GameObjectInactive['Forest'],
##                       GameObjectInactive['Mountain'],GameObjectInactive['Grass']
##                       ]
##        print ('%s img_tile'  %  self.img_tile)
        gui.Terrain.Draw(self,self, scene)
    
    def LoadUnits(self,unit,x,y):
            import bge 
            import bpy
            import gui
            
            scene = bge.logic.getCurrentScene()
            cont = bge.logic.getCurrentController()
            own = cont.owner
            
##            print ('%s scene'  % scene)
##            print ('%s scene'  % scene.objects)
##            print ('%s scene'  % scene.objectsInactive)    
##            print ('%s cont'  % cont)
##            print ('%s own'  % own )
##            for obj in bpy.data.objects:
##                print ('bpy.data.objects %s  '  % obj.name )
                #obj.name = obj.name.replace("Artillery", "ggggggg")
                #print ('bpy.data.objects %s  '  % obj.name )
            GameObjectInactive=scene.objectsInactive
            gui.Units.Draw(unit,scene,x,y)

        
# Starts a new game when launched.
    def main(self, args):
        self.players = [0,1,2,3]
        """ generated source for method main """
        self.npc = [False,True,True,True]
        self.btl.NewGame('FourCorners') 
        self.btl.AddCommanders(self.players, self.npc, 100, 50)
        print ('%s player'  % self.player)
        print ('%s builds'  % self.builds)
        print ('%s units'  % self.units)
        self.LoadTerrain()
        self.GameState=self.State.PLAYING
       




