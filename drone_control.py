from djitellopy import Tello
import time

import keyboard
    


state = None

def control_drone():
    """
    Control Drone using 

        q w e
        a s d
    """

    tello = Tello()
    tello.connect()

    input("Start drone?")

    tello.takeoff()
    keep_running = True

    print("\n\n========\n\n")
    print("Drone is running")

    while keep_running:        
        if keyboard.is_pressed('w') and state != "FWD":
            print("FWD")
            tello.move_forward(100)
            state = "FWD"
        elif keyboard.is_pressed('a') and state != "LEFT":
            print("LEFT")
            tello.move_left(100)
            state = "LEFT"
        elif keyboard.is_pressed('s') and state != "BKWD":
            print("BKWD")
            tello.move_back(100)
            state = "BKWD"
        elif keyboard.is_pressed('d') and state != "RIGHT":
            print("RIGHT")
            tello.move_right(100)
            state = "RIGHT"
        elif keyboard.is_pressed('q') and state != "RL":
            print("R-Left")
            tello.rotate_counter_clockwise(100)
            state = "RL"
        elif keyboard.is_pressed('e') and state != "RR":
            print("R-Right")
            tello.rotate_clockwise(100)
            state = "RR"
        elif keyboard.is_pressed('x'):
            keep_running = False
        else: 
            tello.set_speed(0)
            continue
        time.sleep(0.5)

    tello.land()

if __name__ == "__main__":
    control_drone()
