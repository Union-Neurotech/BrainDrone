import argparse
import time
import os
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
import brainflow

"""
DEMO CODE for using Brainflow and Unicorn

See:
https://brainflow.readthedocs.io/en/stable/Examples.html#python

For more details

- Leo

"""

def parse_config(config_file):
    """
    Checks the local config file and returns it's contents as a dictionary
    """

    dir = os.getcwd()
    config_path = os.path.join(dir, config_file)

    config_dict = {}

    with open(config_path, "r") as f:
        for line in f:
            
            content = line.split(": ")
            print(content)
            config_dict[content[0]] = content[1]

    return config_dict

def run(runtime=10, needsPort=False):
    """
    Records and saves data from the Unicorn Board

    runtime: the time taken for recording
    needsPort: whether we need a serial port or not, the bluetooth dongle functions as bluetooth so likely unneeded
    """

    BoardShim.enable_dev_board_logger()

    params = BrainFlowInputParams()

    config = parse_config("config.dat")

    if needsPort:
        port = config["PORT"]

        new_config = input(f"Use new serial port, or used stored serial port? Stored: {port}")
        if new_config != "":
            port = new_config
        params.serial_port = port
    
    board = BoardShim(BoardIds.UNICORN_BOARD.value, params)
    board.prepare_session()
    board.start_stream()

    time.sleep(runtime)

    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    board.stop_stream()
    board.release_session()
    
    filename = input("What do you want to name your output file?")
    brainflow.DataFilter.write_file(data, f'{filename}.csv', 'w')  # use 'a' for append mode

    print("Data has been saved. Closing.")


if __name__ == "__main__":
    run(runtime=10, needsPort=False)