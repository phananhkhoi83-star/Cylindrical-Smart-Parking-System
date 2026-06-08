<img width="1769" height="1433" alt="image" src="https://github.com/user-attachments/assets/fc2d09fe-ae68-4fc2-92f0-0d2f2b7b3b60" /># Automated Circular Parking Tower 

## 📖 Project Overview
This repository showcases the 3D mechanical design and control system simulation for an **Automated Circular Parking Tower**. The system is designed to optimize urban parking space by utilizing a vertical cylindrical structure with automated lifting and rotating mechanisms.

A full demonstration of the system's operation can be viewed here:
🎥 **[Watch the demo on YouTube: Parking car town cirle systems](https://youtu.be/zNejd4-UcOk?si=oN78pL1fmu8lp_hu)**

## ⚙️ Control Logic & Communication
The core logic of this project integrates hardware identification, precise motor control, and seamless industrial communication between PC and PLC.
* **RFID Identification & Data Processing:** The system utilizes RFID technology to identify incoming vehicles. A Python application reads and processes the RFID signals to determine the appropriate parking slots.
* **PC-PLC Communication (Snap7):** Using the `snap7` library in Python, the processed RFID data and subsequent operational commands are transmitted directly to the Siemens PLC.
* **Stepper Motor Control:** The PLC manages the lifting elevator and rotary platform driven by calculated stepper motor profiles. Position tracking and alignment are handled through algorithmic step-counting to execute predefined parking and retrieval scenarios.

## 📐 Mechanical Structure
* **Central Lifting Elevator:** Vertical transport mechanism to move vehicles up and down the tower.
* **Rotary Platform:** A rotating base that aligns the elevator with the target parking slot based on calculated step data.
* **Cylindrical Framework:** The main structural support designed for stability and space efficiency.

## 📷 Media & Renderings
<img width="1769" height="1433" alt="image" src="https://github.com/user-attachments/assets/cc80d37e-a5e2-4727-877b-884680e946c4" />

## 🛠️ Tools & Technologies Used
* **Automation & PLC Control:** TIA Portal V19, Siemens PLC
* **Programming & Communication:** Python (PyCharm), python-snap7
* **3D CAD Design & Assembly:** SolidWorks 2022
* **Hardware:** RFID Module, Stepper Motors
