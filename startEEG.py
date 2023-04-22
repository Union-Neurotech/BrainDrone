import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter
from brainflow.ml_model import MLModel, BrainFlowMetrics, BrainFlowClassifiers, BrainFlowModelParams
import os
from termcolor import colored
import socket
from djitellopy import Tello

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

def takeoff_drone():
    pass

def land_drone():
    pass

def runEEG_stream(all_live, upper_threshold, lower_threshold, use_drone):
    drone_live = False
    
    if use_drone:
        # Create a Tello object
        tello = Tello()
        # Connect to the drone
        tello.connect()
        print(f"Battery: {tello.get_battery()}")

    if not all_live:
        BoardShim.enable_board_logger()
        DataFilter.enable_data_logger()
        MLModel.enable_ml_logger()
        params = BrainFlowInputParams()

        board_id = BoardIds.UNICORN_BOARD.value()

        board = BoardShim(board_id, params)
        master_board_id = board.get_board_id()
        sampling_rate = BoardShim.get_sampling_rate(master_board_id)

        print("\n\n=================\n\n")

        print("Load ML model:")
        model_params = BrainFlowModelParams(BrainFlowMetrics.USER_DEFINED,
                                                BrainFlowClassifiers.ONNX_CLASSIFIER)

        current_model = "forest_concentration.onnx"
        model_filepath = os.path.join(os.getcwd(), 'models', current_model)

        model_params.file = model_filepath
        model_params.output_name = "probabilities"

        ml_model = MLModel(model_params)

        print(MLModel)

        ml_model.prepare()


        while True:
            
            start = input(colored("Start system? (y/n)", "cyan"))
            if start == "y":
                # Execute connect-device command
                print("Received connect-device command")
                board.prepare_session()

                # Execute start-device command
                print("Received start-device command")
                board.start_stream(45000)

                keep_running = True
                time.sleep(5)

                while keep_running:
                    BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')
                    data = board.get_board_data()
                    eeg_channels = BoardShim.get_eeg_channels(int(master_board_id))
                    bands = DataFilter.get_avg_band_powers(data, eeg_channels, sampling_rate, True)
                    feature_vector = bands[0]    
                    output = ml_model.predict(feature_vector)
                    print(f"Output: {output[0]}")

                    if use_drone:
                        if float(output) > float(upper_threshold):
                            if drone_live == False:
                                tello.takeoff()
                                drone_live = True
                        elif float(output) < float(lower_threshold):
                            if drone_live == True:
                                tello.land()
                                drone_live = False

                    time.sleep(5)  # recommended window size for eeg metric calculation is at least 4 seconds, bigger is better

                    if keyboard.is_pressed("x"):
                        keep_running = False

                import keyboard
                if keyboard.is_pressed("x"):
                    ml_model.release()
                    board.stop_stream()
                    board.release_session()

if __name__ == "__main__":
    all_live = False
    runEEG_stream(all_live, upper_threshold=0.7, lower_threshold=0.3, use_drone=False)