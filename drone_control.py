import time
import keyboard
from djitellopy import Tello

# Create a Tello object
tello = Tello()

# Connect to the drone
tello.connect()

# Print battery status
print(f"Battery: {tello.get_battery()}")

# Ask the user if they want to take off
takeoff = input("Do you want to take off? (y/n): ")
if takeoff.lower() == "y":
    tello.takeoff()
    keep_running = True
else: keep_running = False

# Set the default command to stop the drone
print("BEGIN LOOP")
# Loop until the user presses 'esc' or the program is interrupted
while keep_running:
    if keyboard.is_pressed('w'):
        tello.move_forward(30)
    
    if keyboard.is_pressed('s'):
        tello.move_back(30)
    
    if keyboard.is_pressed('a'):
        tello.move_left(30)
    
    if keyboard.is_pressed('d'):
        tello.move_right(30)

    if keyboard.is_pressed('q'):
        tello.rotate_counter_clockwise(30)

    if keyboard.is_pressed('e'):
        tello.rotate_clockwise(30)

    # Sleep for a short amount of time to avoid using too much CPU
    time.sleep(0.01)

    # Check if the user has pressed 'esc'
    if keyboard.is_pressed("esc"):
        # Land the drone
        tello.land()
        keep_running = False
