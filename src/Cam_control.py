import bge
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
#lclick,always = cont.sensors
scene = bge.logic.getCurrentScene()
oblist = scene.objects
Move= cont.sensors["Move"]
#print ('Move  %s ' % Move.position)
import Rasterizer as R
height = R.getWindowHeight()
width = R.getWindowWidth()
mx = Move.position[0]
my = Move.position[1]

prox = 5

speed = 0.3

if mx > (width-prox):
	dx = speed
	print ('Move  Right %s ' % dx)
	MoveToRight = cont.actuators["MoveToRight"]
	cont.activate(MoveToRight)
elif mx < prox:
	dx = -speed
	print ('Move  Left %s ' % dx)
	MoveToLeft = cont.actuators["MoveToLeft"]
	cont.activate(MoveToLeft)
else:
	dx = 0
	print ('Move  stop %s ' % dx)
	StopMoveToLeft = cont.actuators["StopMoveToLeft"]
	StopMoveToRight = cont.actuators["StopMoveToRight"]
	cont.activate(StopMoveToRight)
	cont.activate(StopMoveToLeft)
#if my > (height-prox):
#	dy = -speed
#elif my < prox:
#	dy = speed
#else:
#	dy = 0
#
#camtar = oblist['CamTarget']
#x,y,z = camtar.position
#camtar.position = [x+dx,y+dy,z]
##adder = cont.actuators["AddTree"]
##cont.activate(adder)