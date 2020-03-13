# Imports
from dronekit import connect, Command, LocationGlobal
from pymavlink import mavutil
import time, sys, argparse, math, json
import matplotlib.pyplot as plt

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

# Storing Data
data = {}
time_frame = []
pitch = []
roll = []
yaw = []
GPS_lat = []
GPS_long = []
GPS_alt = []

# Return aircraft states
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
    time_frame.append(elapsed_time)
    pitch.append(vehicle.attitude.pitch)
    roll.append(vehicle.attitude.roll)
    yaw.append(vehicle.attitude.yaw)
    GPS_lat.append(vehicle.location.global_frame.lat)
    GPS_long.append(vehicle.location.global_frame.lon)
    GPS_alt.append(vehicle.location.global_relative_frame.alt)
    if elapsed_time > 5:
        comm_active = False

#print("%s" %vehicle.location.global_frame)
#print("%s" %vehicle.location.global_relative_frame)

# Store values to JSON
data['time_frame'] = time_frame
data['pitch'] = pitch
data['roll'] = roll
data['yaw'] = yaw
data['latitude'] = GPS_lat
data['longitude'] = GPS_long
data['altitude'] = GPS_alt

vehicle.remove_attribute_listener('attitude', attitude_callback)

# Close vehicle object
vehicle.close()

# Plot results
# Attitude chart
f = plt.figure(1)
plt.plot(time_frame, pitch)
plt.plot(time_frame, roll)
plt.plot(time_frame, yaw)
plt.xlabel('time (sec)')
plt.legend()
f.show()

g = plt.figure(2)
plt.plot(time_frame, GPS_lat)
plt.plot(time_frame, GPS_long)
plt.plot(time_frame, GPS_alt)
plt.xlabel('time (sec)')
plt.legend()
g.show()

raw_input()

# End sitl
print("Completed")
