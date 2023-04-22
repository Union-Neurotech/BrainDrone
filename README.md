# BrainDrone
Brain Activity operated Drone


## Initial Prototype for BR41N.io

## Design

* Script for connecting Unicorn to computer and initating a stream of EEG
* Script for connecting to Tello Drone
    - Connect the two
* Script for connect Frontend UI to Backend

## Setup

1. Create a python virtual environment in the `c:\ ... \BRAINDRONE\` directory using 

    ```bash
    python -m venv .venv
    ```

2. Activate the virtual environment using:

    ```bash
    .venv/Scipts/activate
    ```

3. Install all requirements using:

    ```bash
    pip install -r requirements.txt
    ```

## Running

### For `streaming_test.py`

1. Make sure that your Unicorn (or other EEG device) is connected. You can visit 

