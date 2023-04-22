import os
import subprocess


def start_program(filename):
    
    current_dir = os.getcwd()
    program_path = os.path.join(current_dir, filename)  


    # Define the command to open a new command prompt window and run a Python script
    command = f"start cmd /k python {program_path}"

    # Open a new command prompt window and run the Python script
    subprocess.call(command, shell=True)

if __name__ == "__main__":

    start_program("startDrone.py")
    # start_program("startEEG.py")
    start_program("startUI.py")
    


    