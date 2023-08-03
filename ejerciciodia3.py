import os
import sys
import time
#sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from xarm.wrapper import XArmAPI
arm = XArmAPI('192.168.1.205') #Aqui colocar la IP de nuestro robot.
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.connect()

#arm.reset(wait=True)
arm.set_position(x=-48, y=268, z=491, roll=-180, pitch=0, yaw=0, speed=200, wait=True)

arm.set_cgpio_digital(0, 0, delay_sec=0)
arm.set_position(x=300, y=0, z=150, roll=-180, pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))
arm.set_cgpio_digital(0, 1, delay_sec=0)


## segundo pick
arm.set_position(x=258, y=-0.1, z=501, roll=-180, pitch=0, yaw=0, speed=200, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))

arm.set_position(x=-48, y=268, z=491, roll=-180, pitch=0, yaw=0, speed=200, wait=True)
arm.set_position(x=-48, y=268, z=190, roll=-180, pitch=0, yaw=0, speed=200, wait=True)
arm.set_cgpio_digital(0, 0, delay_sec=0)
# set initial position

arm.set_position(x=-48, y=268, z=491, roll=-180, pitch=0, yaw=0, speed=200, wait=True)