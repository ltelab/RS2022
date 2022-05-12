# EXERCISE for Remote Sensing Course 

This repository contains the exercices for the EPFL Remote Sensing Course.

The exercises can be executed directly on the EPFL NOTO platform. 

Alternatively, you can clone this repository on your laptop and install the required environment using conda with the following steps: 

0. Go to the directory where you want to clone the repository. As an example: 
   ```sh
   cd /home/ghiggi/Courses
   ```
   
1. Clone this repository:
   ```sh
   git clone git@github.com:ltelab/RS2022.git
   cd RS2022
   ```

2. Install the dependencies using conda:
   ```sh
   conda env create -f environment.yml
   ```
   
3. Activate the rs2022 conda environment:
   ```sh
   conda activate rs2022
   ```
   
4. Launch the jupyter notebook:
    ```sh
   jupyter notebook
   ```
   
Note that the installation of the dependencies might cause conflicts; in case you encounter such issues and cannot fix them, please contact the TA team.
