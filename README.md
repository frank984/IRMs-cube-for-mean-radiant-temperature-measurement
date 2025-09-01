# An open-source prototype for measuring Mean Radiant Temperature using low-cost infrared sensor arrays.

![Prospettica\_3D\_slot](https://github.com/user-attachments/assets/8fb18f84-6f67-42e0-9ffe-cbcefc54c811)

## Research Question

Is it possible to measure **Mean Radiant Temperature (MRT)** in a different way from the standard methods defined by **ASHRAE Standard 55** and **ISO 7726**?
These standards typically rely on a reference system consisting of:

* A globe thermometer
* A hot-wire anemometer
* A thermohygrometer

## Our Approach

To explore this question, we designed a prototype based on **six Melexis MLX90640-ESF-BAA infrared sensor modules (IRMs)**, arranged in a cube configuration (see image above).

## First Results

Initial tests at **ZEBlab, ITC-CNR** allowed us to compare measurements from the reference system with those from the new prototype.
The methodology and preliminary results are described in:

> *Low-cost infrared sensor array and open-source hardware for monitoring mean radiant temperature*
> F. Salamone, L. Belussi, L. Danza, S. Sibilio, M. Masullo
> Submitted to **CISBAT 2025 – The Built Environment in Transition**,
> Lausanne, Switzerland, 3–5 September 2025.
> [CISBAT Conference Website](https://cisbat.epfl.ch/)

## Why Open Source?

Further research and testing are needed to validate the system under different configurations.
To support this, we are releasing:

* **[3D-printed support]() design**
* **[Code](https://github.com/frank984/IRMs-cube-for-mean-radiant-temperature-measurement/blob/main/MRT.py) for data acquisition and logging**
* **[Fritzing](https://fritzing.org/) [schematic diagram](https://github.com/frank984/IRMs-cube-for-mean-radiant-temperature-measurement/blob/main/1_rasp_1_PCA9548A_6_MLX90640_cut.png)**

Our goal is to make the system **user-friendly, reproducible, and accessible** for researchers and practitioners.
