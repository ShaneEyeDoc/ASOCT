#This script is generate the pixel intensity sum as a surrogate marker for optical density in FECD patients. 

#Importing the necessary libraries
import numpy as np
import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import math

# Read the CSV file containing image file paths, which also contains the ground truth labelling of FECD grading (0, 1, 2)
image_paths_df = pd.read_csv('img_filpath_od.csv')

#save the column names as a text file
image_paths_df.columns.to_list()

# Define ROI coordinates
roi_top = 100
roi_bottom = 900
roi_left = 0
roi_right = 550

# Initialize a list to store pixel intensity sums
intensity_sums = []

# Initialize a dictionary to store results
intensity_results = {}

# Loop through image paths
for index, row in image_paths_df.iterrows():
    image_path = row['FilePath']
    file_type = row['FileType']
    
    # Check if the file type is 'image/jpeg'
    if file_type == 'image/jpeg':
        # Load the image
        img = cv.imread(image_path, 0)  # Load image as grayscale
        
        if img is not None:
            # Extract the ROI
            roi = img[roi_top:roi_bottom, roi_left:roi_right]
            
            # Calculate the pixel intensity sum within the ROI
            intensity_sum = np.sum(roi)
            
            # Store the result in the dictionary
            intensity_results[image_path] = intensity_sum
        else:
            print(f"Failed to load image: {image_path}")
    else:
        print(f"Skipping non-JPEG file: {image_path}")

# Print or use the results
for image_path, intensity_sum in intensity_results.items():
    print(f"Image Path: {image_path}, Intensity Sum: {intensity_sum}")


# Create a new DataFrame based on image_paths_df and add the 'IntensitySum' column
img_int= image_paths_df.copy()
img_int['IntensitySum'] = img_int['FilePath'].map(intensity_results)

#Save it as a csv file, containing Patient info, DMEK info, OCT measurements, Image paths, and intensity sums
img_int.to_csv('fecd_od.csv', index=False)
