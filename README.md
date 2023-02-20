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
   git clone git@github.com:ltelab/RS2023.git
   cd RS2023
   ```

2. Install the dependencies using conda:
   ```sh
   conda env create -f environment.yml
   ```
   
3. Activate the exo-rs2023 conda environment:
   ```sh
   conda activate exo-rs2023
   ```

4. Add the environment to the jupyter notebook: 
   ```sh
   python -m ipykernel install --user --name=exo-rs2023
   ```

6. Launch the jupyter notebook:
   ```sh
   jupyter notebook
   ```
   
Note that the installation of the dependencies might cause conflicts; in case you encounter such issues and cannot fix them, please contact the TA team.

The latest version of the required packages can be installed using the following command: 
```sh
conda install numpy pandas xarray dask rasterio rioxarray scikit-learn matplotlib-base seaborn colorcet pywavelets pillow jupyter
```
