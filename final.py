import cv2
import numpy as np
import os
import glob

img_array = []

#for filename in glob.glob('data/tennis/.jpg'):
for file in range(1,192):
    img = cv2.imread('tool/bg/'+str(file)+'.jpg')
    print(img)
    
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

    #lsorted = sorted(img_array,key=lambda x: int(os.path.splitext(x)[0]))

    #img_array.sort(key=lambda f: int(filter(str.isdigit, f)))



out = cv2.VideoWriter('walk_bg.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()



    
