# AeroRescue

# Quadcopter for Flood Rescue - Crowd Analysis and Tracking

This repository documents the development of a quadcopter designed to perform crowd analysis for flood rescue operations. The project will begin with an OpenCV-based image recognition system and later evolve to a thermal-based heat signature tracking system. The final goal is to deploy a swarm of drones for accurate, real-time data collection of designated areas.

## 🚀 Project Overview

* **Phase 1:** Development of a 5-inch quadcopter using a Raspberry Pi 5 as the primary payload for real-time image recognition.
* **Phase 2:** Transition to thermal-based tracking and introduction of drone swarm capabilities.
* **Phase 3:** Implementation of swarm management for coordinated data collection across multiple drones.

### Initial Prototype Specifications:

* **Frame Size:** 5-inch quadcopter
* **Flight Controller:** STM32 SpeedyBee F405 V3 running iNav
* **Radio & Telemetry:** ELRS
* **GPS & Compass:** M10 GPS with HMC8883 compass
* **Payload:** Raspberry Pi 5 with camera module
* **Data Processing:** OpenCV/TensorFlow for image recognition
* **Data Visualization:** Google Maps API with graphical/color grading techniques
* **Navigation:** Waypoint navigation of designated geographies

## ✅ Project Objectives

1. Develop a robust image recognition system using OpenCV/TensorFlow to identify crowds in flood-affected areas.
2. Implement waypoint navigation to survey specific geographies autonomously.
3. Design a standalone web interface to display real-time data using graphical and color grading techniques on Google Maps.
4. Transition to a thermal-based tracking system to enhance target detection capabilities.
5. Develop a swarm management protocol for synchronized data collection and analysis across multiple drones.
6. Integrate QGroundControl for more advanced mission planning and data visualization.

## 🛠️ Technology Stack

* **Programming Languages:** Python, C/C++
* **Libraries/Frameworks:** OpenCV, TensorFlow, iNav, QGroundControl, Google Maps API
* **Communication Protocols:** ELRS, Ublox, MAVLink (in later versions)
* **Hardware:** Raspberry Pi 5, STM32 SpeedyBee F405 V3, ELRS modules, GPS module, camera, thermal sensor (future implementation)

## 🌐 Future Development

* Implement thermal signature tracking for enhanced detection in low-visibility scenarios.
* Develop a swarm management system for data synchronization and collective analysis.
* Transition to QGroundControl for mission planning, monitoring, and data visualization.

Stay tuned for updates as we progress through each phase of the project.
 
