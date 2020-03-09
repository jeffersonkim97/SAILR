# Imports
import time
from dronekit import connect, VehicleMode

# Setup
connection_string = "/dev/ttyACM0"
baud_rate = 115200

# Establishing vehicle connection
print("start connection...")
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, baud = baud_rate, wait_ready=True)

# Return vehicle attributes (State)
print("Vehicle attribute values:")
print("  GPS: %s" % vehicle.gps_0)
print("  Last Heartbeat: %s" % vehicle.last_heartbeat)
print("  System status: %s" % vehicle.system_status.state)
print("  Mode: %s" % vehicle.mode.name)

def attitude_callback(self, attr_name, value):
    print(vehicle.attitude)

print("")
print("Adding an attitude listener")
vehicle.add_attribute_listener('attitude', attitude_callback)
time.sleep(5)

vehicle.remove_attribute_listener('attitude', attitude_callback)

# Close vehicle object
vehicle.close()

# End sitl
print("Completed")
