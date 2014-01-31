from __future__ import absolute_import
import sys,os
#print ("%s" % sys.path)


import bge
##cont = bge.logic.getCurrentController()
##adder = cont.actuators["Gameloop"]
##print("%s" %adder)
def main():
    from engine.Game import Game
    print ("%s" %"Play")
    BegGame=Game()
    global BegGame
    BegGame.main(sys.argv)
    
def GameStatePlay():
    cont = bge.logic.getCurrentController()
    click = cont.sensors["Click"]
    over  = cont.sensors["Over"]
    if click.positive and over.positive:
        print("%s" %"Start_Game.GameStatePlay")
        BegGame.btl.EndTurn()
        
        #adder = cont.actuators["EndTurnToFalse"]
        #cont.activate(adder)
    
def Gameloop():
    #print("%s" %"Starting Gameloop...")
    BegGame.GameLoop()
#cont.activate(adder)
#threads = threading.Thread(name="Prod 1" , target=BegGame.main,args=(sys.argv,)) 
#print("%s" %"Starting threads...")
#threads.start()
#print("%s" %"Waiting for threads to finish...")
#threads.join()
##
##print ("%s" %"Play")