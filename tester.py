from gridappsd import GridAPPSD
import time
#def on_message_callback(header, message):
#    print(f"header: {header} message: {message}")
def on_message_callback(header, message):
    username = header.get('username', 'Unknown')  # Extract username from header

# Note these should be changed on the server in a cyber secure environment!
#username = "system"
#password = "manager"
username = "app_user"
password = "1234App"
# Note: there are other parameters for connecting to
# systems other than localhost
gapps = GridAPPSD(username=username, password=password)

assert gapps.connected

gapps.send('send.topic', {"foo": "bar"})

# Note we are sending the function not executing the function in the second parameter
gapps.subscribe('subscribe.topic', on_message_callback)

gapps.send('subcribe.topic', 'A message about subscription')

time.sleep(5)

#gapps.close()
gapps.disconnect()  # Disconnect from the GridAPPSD service