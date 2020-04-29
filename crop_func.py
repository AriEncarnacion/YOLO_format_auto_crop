import os
import cv2
from PIL import Image


def crop_func(file, all_labels, idx, new_path):
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

    print("Image dimensions:", img.shape)
    img_h = img.shape[0]
    img_w = img.shape[1]

    box_x = img_w * center_x  # convert YOLO format back to pixel value
    box_y = img_h * center_y
    box_w = img_w * width
    box_h = img_h * height
    print("Exact box coordinates:", box_x, box_y, box_w, box_h)

    left = int(box_x - box_w / 2)  # calculate bounding box coordinate and put in int form for pixels
    bottom = int(box_y + box_h / 2)
    right = int(box_x + box_w / 2)
    top = int(box_y - box_h / 2)
    print("Pixel coordinates for cropping...")
    print(F"start_x: {left}, end_x: {right}, start_y: {top}, end_y: {bottom}")

    crop_img = pil_im.crop((left, top, right, bottom))  # crop the image

    crop_img.save(new_path + img_name)
    print("Saving at directory:", new_path)
    print()
