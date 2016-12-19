import cv2
import numpy as np
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('search_directory', action="store")
parser.add_argument('move_to', action="store")
parser.add_argument('compare_file', action="store")
parser.add_argument('date_name', action="store")
results = parser.parse_args()

file1 = cv2.imread(results.compare_file)
for filename in os.listdir(results.search_directory):
    file2 = cv2.imread(filename)
    if np.shape(file1) == np.shape(file2):
        file_comparison = cv2.subtract(file1, file2)
    else:
        continue
    same_image = not np.any(file_comparison)
    if same_image is True:
        print("moving")
        shutil.move(search_directory+filename, results.move_to+results.date_name)
        exit()
