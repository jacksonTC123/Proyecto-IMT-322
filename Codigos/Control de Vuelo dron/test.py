from DroneController import Drone

drone = Drone()

drone.connect()
drone.calibrate()
drone.take_off(wait=1)  

drone.move('forward', speed=50, wait=1) 

drone.move('backward', speed=50, wait=2)
drone.rotate('left', speed=50,wait=1)
drone.move("up",speed=50,wait=1)
drone.rotate('right', speed=50,wait=1)

drone.land(wait=2)  

drone.disconnect()  

