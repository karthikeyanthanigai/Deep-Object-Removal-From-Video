import cv2
import numpy as np
import os
import glob

img_array = []

#for filename in glob.glob('data/tennis/.jpg'):
for file in sorted(os.listdir('data/tennis/')):
    img = cv2.imread(os.path.join('data/tennis/', file))
    print(img)
    
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

    #lsorted = sorted(img_array,key=lambda x: int(os.path.splitext(x)[0]))

    #img_array.sort(key=lambda f: int(filter(str.isdigit, f)))



out = cv2.VideoWriter('walk.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()



    
