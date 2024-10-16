# **Pixel Intensity Analysis for Optical Density in FECD Patients**

This project aims to calculate pixel intensity sums as a surrogate marker for optical density in patients with Fuchs' Endothelial Corneal Dystrophy (FECD) using images and Region of Interest (ROI) selection. The pixel intensity is used as an approximate measure of corneal opacity, which can provide insights into disease progression.

## **Project Overview**

The script processes a list of images associated with FECD patients, computes the pixel intensity sum within a specified region of interest (ROI), and stores the results in a CSV file. This can be further used to analyze correlations between image pixel intensities and clinical markers for FECD such as corneal thickness, DMEK surgery status, and OCT (Optical Coherence Tomography) measurements.

## **File Structure**

- **img_filpath_od.csv**: CSV file containing image file paths and metadata (such as patient information, FECD grading, and image type).
- **fecd_od.csv**: The output file that stores patient info, DMEK info, OCT measurements, image paths, and the calculated pixel intensity sums for each image.
  
## **Requirements**

- Python 3.x
- Libraries:
  - `numpy`: For numerical operations.
  - `opencv-python` (`cv2`): For reading and processing images.
  - `Pillow` (`PIL`): For image handling (optional).
  - `matplotlib`: For any potential visualization of the results.
  - `pandas`: For handling CSV files and DataFrame operations.


## **Workflow**

1. **Input Data**:
    - The input CSV file (`img_filpath_od.csv`) contains the paths to the images and associated metadata such as FECD grading, patient information, DMEK status, etc.
  
2. **ROI Definition**:
    - The region of interest (ROI) is hard-coded in the script and defined by the coordinates:
      - **Top**: 100 pixels
      - **Bottom**: 900 pixels
      - **Left**: 0 pixels
      - **Right**: 550 pixels
    - The ROI is extracted from each image for calculating pixel intensity sums.

3. **Processing**:
    - The script processes images, particularly those in **JPEG format** (`image/jpeg`).
    - For each valid image, the pixel intensity sum within the defined ROI is calculated and stored.

4. **Output**:
    - The results are saved in `fecd_od.csv`, which includes patient info, DMEK info, OCT measurements, image paths, and the pixel intensity sum for each image.

