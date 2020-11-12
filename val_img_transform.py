import cv2
import numpy as np
import os

for img_name in os.listdir('datasets/coco_stuff/val_img'):
    img = cv2.imread('datasets/coco_stuff/val_img/'+img_name)
    black = np.zeros((img.shape))
    cv2.imwrite('datasets/coco_stuff/val_img/'+img_name, black)
