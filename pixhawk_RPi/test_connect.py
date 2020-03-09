# Imports
import dronekit_sitl
from dronekit import connect, VehicleMode

# Setup
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Establishing vehicle connection
print("start connection...")
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

# Return vehicle attributes (State)
print("Vehicle attribute values:")
print("  GPS: %s" % vehicle.gps_0)
print("  Last Heartbeat: %s" % vehicle.last_heartbeat)
print("  System status: %s" % vehicle.system_status.state)
print("  Mode: %s" % vehicle.mode.name)

# Close vehicle object
vehicle.close()

# End sitl
sitl.stop()
print("Completed")
