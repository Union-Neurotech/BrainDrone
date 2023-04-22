import Image from "next/image";
import { Roboto_Mono } from "next/font/google";
import { useState } from "react";
const inter = Roboto_Mono({ subsets: ["latin"] });

//adding a slider

export default function Home() {
  const [connectedHeadset, setConnectedHeadset] = useState(true);
  const [connectedDrone, setConnectedDrone] = useState(true);
  const [droneState, setDroneState] = useState(1);
  const [droneData, setDroneData] = useState(1);
  const [headsetData, setHeadsetData] = useState(0);
  const [progressPercentage, setProgressPercentage] = useState(70);
  const [pressedKey, setPressedKey] = useState("");

  const handleKeyDown = (event) => {
    if (event.key === "w") {
      setPressedKey("w");
    } else if (event.key === "a") {
      setPressedKey("a");
    } else if (event.key === "s") {
      setPressedKey("s");
    } else if (event.key === "d") {
      setPressedKey("d");
    }
  };

  const handleKeyUp = (event) => {
    setPressedKey("");
  };

  const connectToDevice = async (deviceName) => {
    try {
      const device = await navigator.bluetooth.requestDevice({
        filters: [{ name: deviceName }],
      });

      const server = await device.gatt.connect();
      // Do something with the server object
      console.log("Connected to device:", deviceName);

      if (deviceName === "Headset") {
        setConnectedHeadset(true);
      } else if (deviceName === "Drone") {
        setConnectedDrone(true);
      }
    } catch (error) {
      console.error("Error connecting to device:", error);
    }
  };
  return (
    <main
      className={`flex h-screen w-full flex-col items-center justify-between p-24 ${inter.className} bg-[#141C41] overflow-y-hidden`}
      onKeyDown={handleKeyDown}
      onKeyUp={handleKeyUp}
      tabIndex={0}
    >
      <div className="flex flex-col items-center gap-4 w-screen">
        <h1 className="text-4xl font-semibold">BrainDrone</h1>
        <p>By Union NeuroTech</p>
        <hr className="mt-2 w-3/4" />
      </div>
      <div className="flex flex-row justify-between items-center gap-8 mt-16 w-full">
        <div className="flex flex-col gap-2 items-center">
          <p className=" text-center font-bold">Controls:</p>
          <ul className="text-center">
            <li>Forwards: W</li>
            <li>Back: S</li>
            <li>Left: A</li>
            <li>Right: D</li>
            <li>Take Off: Concentrate</li>
            <li>Land: Relax</li>
            <li>Rotate: By moving head</li>
          </ul>
        </div>
        <div className="flex flex-col gap-2 items-center">
          <h1>Headset</h1>
          <Image
            src="/brain.png"
            width={300}
            height={300}
            alt="Union NeuroTech Brain Icon"
          />
          {connectedHeadset ? (
            <div className="flex flex-col gap-2 items-center">
              <p className="flex flex-row items-center">
                You are connected!
                <Image
                  src="/checkmark.png"
                  width={50}
                  height={50}
                  alt="Check"
                />
              </p>
              {headsetData ? (
                <div className="flex flex-row items-center">
                  You are streaming!
                  <Image
                    src="/checkmark.png"
                    width={50}
                    height={50}
                    alt="Check"
                  />
                </div>
              ) : (
                <>Loading stream...</>
              )}
              <button
                className="bg-blue-500 text-white font-semibold p-2 rounded-xl w-64 mt-4 hover:scale-105 duration-150"
                onClick={() => {
                  setConnectedHeadset(false);
                }}
              >
                Disconnect
              </button>
            </div>
          ) : (
            <button
              className="bg-blue-500 text-white font-semibold p-2 rounded-xl w-64 mt-4 hover:scale-110 duration-150"
              onClick={() => connectToDevice("Headset")}
            >
              Connect
            </button>
          )}
        </div>
        <div className="flex flex-row gap-2 items-center">
          <div className="flex flex-col gap-2 items-center">
            <h1>Drone</h1>
            <Image
              src="/drone2.png"
              width={300}
              height={300}
              alt="Union NeuroTech Brain Icon"
            />
            {connectedDrone ? (
              <div className="flex flex-col items-center gap-2">
                <p className="flex flex-row items-center">
                  You are connected!
                  <Image
                    src="/checkmark.png"
                    width={50}
                    height={50}
                    alt="Check"
                  />
                </p>
                <p className="flex flex-row items-center">
                  {droneData ? (
                    <>
                      You are streaming!
                      <Image
                        src="/checkmark.png"
                        width={50}
                        height={50}
                        alt="Check"
                      />
                    </>
                  ) : (
                    <>Loading stream...</>
                  )}
                </p>
                <button
                  className="bg-blue-500 text-white font-semibold p-2 rounded-xl w-64 mt-4 hover:scale-105 duration-150"
                  onClick={() => {
                    setConnectedDrone(false);
                  }}
                >
                  Disconnect
                </button>
              </div>
            ) : (
              <button
                className="bg-blue-500 text-white font-semibold p-2 rounded-xl w-64 mt-4 hover:scale-110 duration-150"
                onClick={() => connectToDevice("Drone")}
              >
                Connect
              </button>
            )}
          </div>
        </div>
        <div className="flex flex-col gap-2 items-center">
          <button
            className="text-3xl p-2 rounded-3xl h-16 w-16 shadow-xl"
            style={{
              backgroundColor: pressedKey != "w" ? "#1e3b8a" : "#3B82F6",
            }}
          >
            W
          </button>
          <div className="flex flex-row gap-16">
            <button
              className="text-3xl p-2 rounded-3xl h-16 w-16 shadow-xl"
              style={{
                backgroundColor: pressedKey != "a" ? "#1e3b8a" : "#3B82F6",
              }}
            >
              A
            </button>
            <button
              className="text-3xl p-2 rounded-3xl h-16 w-16 shadow-xl"
              style={{
                backgroundColor: pressedKey != "d" ? "#1e3b8a" : "#3B82F6",
              }}
            >
              D
            </button>
          </div>
          <button
            className="text-3xl p-2 rounded-3xl h-16 w-16 shadow-xl"
            style={{
              backgroundColor: pressedKey != "s" ? "#1e3b8a" : "#3B82F6",
            }}
          >
            S
          </button>
        </div>
      </div>
      <button className="pl-2 pr-2 h-14 flex flex-row items-center bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-xl hover:scale-110 duration-150  shadow-xl">
        <p className="font-bold">Kill Switch</p>
        <div className="h-16 w-16 mt-3">
          <Image src="/warning.png" width={100} height={100} alt="Warning" />
        </div>
      </button>
    </main>
  );
}
