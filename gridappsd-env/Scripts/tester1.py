from gridappsd import GridAPPSD
import time

def on_message_callback(header, message):
    username = header.get('username', 'Unknown')  # Extract username from header or default to 'Unknown'
    print(f"Received message: {message} from {username}")
    print(f"Header: {header}")

try:
    username = "app_user"
    password = "1234App"

    gapps = GridAPPSD(username=username, password=password)
    assert gapps.connected

    gapps.send('send.topic', {"foo": "bar"})

    gapps.subscribe('subscribe.topic', on_message_callback)

    gapps.send('subscribe.topic', 'A message about subscription')

    time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

finally:
    gapps.disconnect()  # Disconnect from the GridAPPSD service
