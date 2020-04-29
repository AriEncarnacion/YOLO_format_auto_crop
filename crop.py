import os
import sys
from crop_func import crop_func
from get_directories import get_directories
import labels as lbl

labels_path = str(sys.argv[1])  # path to label.txt files
data_path = str(sys.argv[2])  # path to images
save_path = str(sys.argv[3])  # path to save the cropped directory

labels_dir, data_dir = get_directories(labels_path, data_path)
all_labels = lbl.get_labels(labels_path, labels_dir)

print("all labels...")
idx = 0
for i in all_labels:
    print(F"File #{idx}")
    for row in i:
        print(row)
    idx += 1

print()

print("Attempting to create cropped directory")
if os.path.exists(save_path):
    print(F"{save_path} already exists.")
else:
    try:
        os.mkdir(save_path)
    except OSError:
        print(F"Creation of the directory '{save_path}' failed.")
    else:
        print(F"Successfully created the directory '{save_path}'.")

print()

idx = 0
for file in data_dir:
    if file.endswith(".jpg"):
        crop_func(file, all_labels, idx, save_path)
        idx += 1
