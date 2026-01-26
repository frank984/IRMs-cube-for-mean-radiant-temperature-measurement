# An open-source prototype for measuring Mean Radiant Temperature using low-cost infrared sensor arrays

![real_vs_3D_render](https://github.com/user-attachments/assets/ebb85bfd-48d3-4495-81c8-4ae733154beb)


## Research Question

Is it possible to measure **Mean Radiant Temperature (MRT)** in a different way from the standard methods defined by **ASHRAE Standard 55** and **ISO 7726**?
These standards typically rely on a reference system consisting of:

* A globe thermometer
* A hot-wire anemometer
* A thermohygrometer

## Our Approach

To explore this question, we designed a prototype based on **six [Adafruit Melexis MLX90640-ESF-BAA infrared sensor modules](https://www.adafruit.com/product/4469) (IRMs)**, arranged in a cube configuration (see image above).

## First Results

Initial tests at **ZEBlab, ITC-CNR** allowed us to compare measurements from the reference system with those from the new prototype.
The methodology and preliminary results are described in:

> *Low-cost infrared sensor array and open-source hardware for monitoring mean radiant temperature*
> F. Salamone, L. Belussi, L. Danza, S. Sibilio, M. Masullo. <br /> 
> The full article is available [here](https://iopscience.iop.org/article/10.1088/1742-6596/3140/8/072023). <br /> 
> Submitted to **CISBAT 2025 – The Built Environment in Transition**,
> Lausanne, Switzerland, 3–5 September 2025.
> [CISBAT Conference Website](https://cisbat.epfl.ch/).<br />
>If you use this page to define your monitoring system, please cite the related article (DOI: http://doi.org/10.1088/1742-6596/3140/8/072023) along with this repository [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17130661.svg)]
> (https://doi.org/10.5281/zenodo.17130661)
> <br />


Author Contributions
- Francesco Salamone: Conceptualization, Methodology, Data curation, Validation, Visualization, Writing – original draft, Writing – review & editing, Design and development of the IRMs cube
- Lorenzo Belussi: Methodology, Data curation, Validation, Writing – original draft, Writing – review & editing
- Ludovico Danza: Methodology, Data curation, Validation, Writing – original draft, Writing – review & editing, provided the funds to purchase infrared modules
- Sergio sibilio: Conceptualization, Methodology, Data curation, Validation, Visualization, Writing – original draft, Writing – review & editing
- Massimiliano Masullo: Conceptualization, Methodology, Data curation, Validation, Visualization, Writing – original draft, Writing – review & editing

## Why Open Source?

Further research and testing are needed to validate the system under different configurations.
To support this, we are releasing:

* **[3D-printed support](https://github.com/frank984/IRMs-cube-for-mean-radiant-temperature-measurement/blob/main/mlx90640_x6_support_3D_printer.stl) design**
* **[Code](https://github.com/frank984/IRMs-cube-for-mean-radiant-temperature-measurement/blob/main/MRT.py) for data acquisition and logging**
* **[Fritzing](https://fritzing.org/) [schematic diagram](https://github.com/frank984/IRMs-cube-for-mean-radiant-temperature-measurement/blob/main/1_rasp_1_PCA9548A_6_MLX90640.png)**

Our goal is to make the system **user-friendly, reproducible, and accessible** for researchers and practitioners.


## CC Attribution-NonCommercial 4.0 International

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc]

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg
