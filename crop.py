import os
import sys
import cv2
from PIL import Image

labels_path = str(sys.argv[1])
data_path = str(sys.argv[2])
save_path = str(sys.argv[3])

labels_dir = os.listdir(labels_path)
data_dir = os.listdir(data_path)

for file in labels_dir:
    if not file.endswith(".txt"):
        print(F"{file} was not a .txt file. Please remove this file from the directory and try again.")
        sys.exit(1)

for file in data_dir:
    if not file.endswith(".jpg"):
        print(F"{file} was not a .jpg file. Please remove this file from the directory and try again.")
        sys.exit(2)

labels_dir.sort()
data_dir.sort()

for i in range(len(data_dir)):
    img = data_dir[i]
    data_dir[i] = data_path + img

print(data_dir)

all_labels = []
for file in labels_dir:
    labels = []
    if file.endswith(".txt"):
        f_path = labels_path + file

        print("opening file at path:", f_path)
        with open(f_path) as f:
            data = f.readlines()
            for line in data:
                labels.append(line.strip().split(" "))

        for row in labels:
            print(row)

        all_labels.append(labels)
        print()
print("LABEL PARSING SUCCESSFULLY COMPLETED.")
print()

print("all labels...")
idx = 0
for i in all_labels:
    print(F"File #{idx}")
    for row in i:
        print(row)
    idx += 1

print()

new_path = save_path + "cropped/"
try:
    os.mkdir(new_path)
except OSError:
    print(F"Creation of the directory '{new_path}' failed.")
else:
    print(F"Successfully created the directory '{new_path}'.")

print()

idx = 0
for file in data_dir:
    if file.endswith(".jpg"):
        img_name = os.path.basename(os.path.normpath(file))
        print(F"Cropping {img_name} at directory {file}")
        img = cv2.imread(file)
        print("Label for image:", all_labels[idx][0])
        pil_im = Image.open(file)

        box = all_labels[idx][0]
        center_x = float(box[1])
        center_y = float(box[2])
        width = float(box[3])
        height = float(box[4])
        # print(type(center_x), type(center_y), type(width), type(height))

        print("Image dimensions:", img.shape)
        img_h = img.shape[0]
        img_w = img.shape[1]

        box_x = img_w * center_x
        box_y = img_h * center_y
        box_w = img_w * width
        box_h = img_h * height
        print("Exact box coordinates:", box_x, box_y, box_w, box_h)

        left = int(box_x - box_w / 2)
        bottom = int(box_y + box_h / 2)
        right = int(box_x + box_w / 2)
        top = int(box_y - box_h / 2)
        print("Pixel coordinates for cropping...")
        print(F"start_x: {left}, end_x: {right}, start_y: {top}, end_y: {bottom}")
        # crop_img = img[crop_start_y:crop_end_y, crop_start_x:crop_end_x].copy()
        crop_img = pil_im.crop((left, top, right, bottom))
        print()
        crop_img.save(new_path + img_name)
        os.chdir(new_path)
        print("Saving at directory:", new_path)
        print()
    idx += 1
