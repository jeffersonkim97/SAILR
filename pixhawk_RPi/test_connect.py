# Imports
from dronekit import connect, Command, LocationGlobal
from pymavlink import mavutil
import time, sys, argparse, math

# Python Function
def attitude_callback(self, attr_name, value):
    """
    Return current pixhawk attitude
    @param attr_name: name of attitude (pitch, roll, yaw)
    @param value: attitude value
    """
    print(vehicle.attitude)

# Setup
connection_string = "/dev/ttyS0"
baud_rate = 921600

# Establishing vehicle connection
print("Start connection...")
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, baud = baud_rate, wait_ready=False) #
vehicle.wait_ready(True, timeout=300)
print("Vehicle connected!")
comm_active = True

#while comm_active:
    # Return vehicle attributes (State)
    #print("")
    #print("Adding an attitude listener")
    #vehicle.add_attribute_listener('attitude', attitude_callback)


print(vehicle.gps_0)
print(vehicle.mode)

start = time.time()
elapsed_time = 0
while comm_active:
    print("===================")
    print("At time %s" %elapsed_time)
    print("%s" %vehicle.attitude)
    print("%s" %vehicle.location.global_frame)
    time.sleep(1)
    end = time.time()
    elapsed_time = end - start
    comm_active = False


#print("%s" %vehicle.location.global_frame)
#print("%s" %vehicle.location.global_relative_frame)

time.sleep(5)

vehicle.remove_attribute_listener('attitude', attitude_callback)

# Close vehicle object
vehicle.close()

# End sitl
print("Completed")
