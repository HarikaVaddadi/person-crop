## Person Cropping from Videos using YOLOv5
This repository contains code and instructions to detect persons in videos using the YOLOv5 object detection model, apply padding to the detected bounding boxes, and save the cropped person images to an output folder.


## Introduction
The goal of this project is to automatically detect persons in videos, apply padding to the bounding boxes to ensure complete coverage of the person, and save the cropped person images. This can be useful for various applications such as surveillance, activity recognition, and more.


## Usage
Place your video files in the input_videos directory.

Run the script to start processing videos and cropping persons:

```bash
$ python detect.py --source input_videos/ --conf-thres 0.4 --classes 0 --save-crop --project output_images/ --name personcrops/ --nosave
```


## Output
Cropped person images will be saved in the output_images directory. The filenames will reflect the frame number from the original video.
