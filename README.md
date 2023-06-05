# Autonomous-Package-Delivery-Drone

## Overview
In today's fast-paced world, drones have emerged as a versatile solution for efficient and timely services. From agricultural analysis to military operations, their applications are widespread. This project focuses on the development of an autonomous hexacopter capable of delivering essentials like medicines, food, vaccines, and organs within city limits.

## Steps Involved
### Simulation using ROS-Gazebo
The project utilizes ROS-Gazebo for simulation purposes, leveraging the PX4 plugin. A hexacopter model is imported into the Gazebo world, and simulation is initiated through a bash script. The script launches the PX4 plugin and a GUI interface where pickup and drop-off locations are provided. These locations are then mapped to their corresponding latitudes and longitudes and fed to PX4 for drone navigation within Gazebo.

### Hardware Implementation
The hardware implementation involves PX4 and Jetson Nano. The Jetson Nano acts as the brain of the system, responsible for path planning and sending drop-off and pickup locations to the PX4 controller. The PX4 controller, in turn, controls the BLDC motors by utilizing feedback from inbuilt MPU sensors and applying PID algorithms to reach the specified coordinates. Pickup and drop-off locations can be given through a mobile application or a web dashboard.

## Specifications
The primary objective of this project is to deliver packages weighing up to 1.5 kg from one hospital to another designated hospital. The package's delivery instructions are scanned using a camera, and character recognition techniques are employed for extracting the block or building name. Commands are then given to the drone based on the chosen optimum path. Waypoints generated through path planning guide the drone along the estimated path.

Spatial data and derived parameters are obtained from the camera and sensors placed at various orientations to map the environment accurately. The Inertial Measurement Unit (IMU) provides reference direction, contributing to drone orientation stabilization through feedback to the controller. Sensor fusion techniques are implemented to obtain precise data from various sensors, including IMUs, GPS, and radar.

Obstacle detection plays a critical role in navigating through dynamic environments. Objects are detected and traversed, and the drone receives further commands based on the entity's size or speed. Predetermined goal points, covering major buildings/hostels of the campus, feature unique target marks (e.g., crosses). After maneuvering to the estimated target spot using image processing, the drone locates the mark and prepares for landing.

For testing purposes, a model environment will be set up in ROS Gazebo, closely resembling real-world scenarios. The drone is designed using SolidWorks, and component calculations are performed considering constraints such as motor rating and propeller specifications. This close-to-real-world setup enables simulation, testing algorithm efficiency, and making necessary optimizations.

## Different Domains
### Drone Design:

Designing the drone with components
Drone calculation
URDF/SDF file generation
Hard code simulation

### ROS - Gazebo:

Navigating to a point
Enabling sensor plugins
Implementing basic obstacle avoidance
Integrating real-world map into Gazebo

### Path Planning:

Researching different path planning algorithms and selecting the most suitable one
Assigning different teams to work on multiple ideas if necessary
Evaluating the optimal algorithm and providing various test cases
Implementing 2D to 3D mapping

### Obstacle Avoidance:

Research and development of stereo/monocular techniques
Developing functional algorithms using hardware, preferably in Python or other languages
Optimizing algorithms using different test cases
Final implementation of obstacle avoidance in Gazebo
