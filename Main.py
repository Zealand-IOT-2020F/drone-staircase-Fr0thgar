import Drone
import sys
import time

# Live drone
#drone_1 = drone.Drone("128.1.1.1", 8889)

# Test drone
# drone start up
drone_1 = Drone.Drone('192.168.10.1', 8889)
drone_1.printInfo(1)
drone_1.connect(1)

#region old
# # Print out start information
# print(drone_1.battery(0.1))
# print(drone_1.time(0.1))
# print(drone_1.sdk(0.1))
# print(drone_1.sn(0.1))

# # Drone flightplan
# drone_1.takeOff(1)
# drone_1.cw("90", 1)
# drone_1.ccw("360", 1)
# drone_1.cw("180", 1)
# drone_1.up("60", 1)
# #drone_1.flip("b", 1)
# drone_1.down("30", 1)
# drone_1.left("20", 1)
# drone_1.right("20", 1)

# # print out landing information
# print(drone_1.battery(0.1))
# print(drone_1.time(0.1))

# # Landing sequence
# drone_1.land(1)
# drone_1.end(1)
#endregion

# Staircase climb up #
# 15 trin 5 - 5 - 5 n
# Forventet Løsning for Martins trappe
# 5 trin op - drej 90C til venstre - 5 trin op - drej 90C til venstre - 5 trin op
# 19 cm høj - (ca. 34 cm / 46 cm (24 cm i gennesnit i midten))? dyb - 85 cm bred
drone_1.takeOff(1)

i = 3

while i < 3:
    # Trin 1-6-11
    drone_1.stepUp(1)
    # Trin 2-7-12
    drone_1.stepUp(1)
    # Trin 3-8-13
    drone_1.stepUp(1)
    # Trin 4-9-14
    drone_1.stepUp(1)
    # Trin 5-10
    drone_1.stepUp(1)
    
    # drej 90C
    drone_1.left("90", 1)


# Lav det dynamisk
# Hvor mange trin er der

# Hvor mange trin før den skal dreje x antal gange

# Hvilken vej skal dronen dreje