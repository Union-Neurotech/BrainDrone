from djitellopy import Tello




def control_drone():

    tello = Tello()
    
    input("Press enter to connect to Tello Drone")

    tello.connect()


    while True:

        command = input("Input a command ( 'u' for UP, anything else for LAND )")

        if command != 'u':
            tello.land()

        else:
            tello.takeoff()




if __name__ == "__main__":
    control_drone()
