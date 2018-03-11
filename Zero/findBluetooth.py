#http://people.csail.mit.edu/albert/bluez-intro/c212.html
#python2
import bluetooth

target_name = "My Phone"
target_address = None

nearbyDevices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
  if target_name == bluetooth.lookup_name( bdaddr ):
    target_address = bdaddr
    break

if target_address is not None:
  print "found target bluetooth device with address ", target_address
else:
  print "could not find target bluetooth device nearby"
