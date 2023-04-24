## Walking Mechanism with Jansen Mechanism using ROS and Dynamixel Motors
This project aims to develop an 8-legged walking mechanism using the Jansen mechanism. The Jansen mechanism is a mechanical linkage that is designed to generate a walking motion similar to that of a spider. The mechanism consists of eight legs, with each leg having three joints.

ROS (Robot Operating System) will be used to control the movement of the walking mechanism. The mechanism will be powered by two Dynamixel motors, which are known for their precision and control.

Additionally, an Xbox controller will be used to control the walking mechanism. The controller will send commands to ROS, which will then send commands to the Dynamixel motors to control the movement of the mechanism.

### Hardware Requirements
1. 2 Dynamixel motors
2. Arduino UNO, esp32 cam module or similar single-board computer
3. Xbox controller
4. 3D-printed parts for the Jansen mechanism

### Software Requirements
1. ROS noetic or later
2. Dynamixel SDK
3. Xbox controller driver for ROS

### Installation
1. Install ROS Kinetic or later on the Raspberry Pi.
2. Install the Dynamixel SDK.
3. Install the Xbox controller driver for ROS.
4. Print the 3D parts for the Jansen mechanism.
5. Assemble the Jansen mechanism using the 3D printed parts and Dynamixel motors.

### Usage
* Connect the Dynamixel motors to the Arduino.
* Connect the Xbox controller to the Arduino.
* Launch ROS on the Arduino.
* Launch the Xbox controller driver for ROS.
* Send commands from the Xbox controller to ROS to control the walking mechanism.

### References
[Jansen Mechanism](https://en.wikipedia.org/wiki/Jansen%27s_linkage) </br>
[ROS](https://www.ros.org/) </br>
[Dynamixel Motors](https://emanual.robotis.com/docs/en/dxl/overview/) </br>
[Xbox Controller Driver for ROS](http://wiki.ros.org/joy)
