# Automatic ROI Cropping System

This script crops an image to an ROI using YOLOv3 format .txt files, OpenCV and Pillow. 

Essentially, an image is cropped to the region outlined by a YOLO output bounding box.

## Usage
**Note this script was built using python 3.7**

This script requires os, cv2 and PIL packages be installed.

Clone this repo and run the following command.

```python3 crop.py <path to directory holding YOLO format .txt files> <path to images> <desired save path>```
**Note each directory must end with a forward slash**

for example

```python3 crop.py ~/Users/usr/labels/ ~/Users/usr/images/ ~/Users/usr/mySaveDir```

And you're done!
