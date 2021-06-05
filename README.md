# Deep-Object-Removal-From-Video

Being vanished is something which is done with magic wands , but there’s one magic wand which will make your object disappear from the video. The techniques we are using are Fast online object tracking and segmentation is the first part of the project. This approach is used to mask the selected object. In this method we compare object with each and every frame which helps to mask the object inside the boundary box. The project has both scientific and ethical goals . 
Secondly, the next part is deep video inpainting which helps us to complete our project successfully that is to remove the selected object with the help of Dip-Vid-Flow.

# How to Run:
## masking
### Setup python environment
```
conda create -n siammask python=3.6
source activate siammask
pip install -r requirements.txt
bash make.sh
```

### Add the project to your PYTHONPATH
```
export PYTHONPATH=$PWD:$PYTHONPATH
```
### Download the SiamMask model
```
cd $SiamMask/experiments/siammask_sharp
wget http://www.robots.ox.ac.uk/~qwang/SiamMask_VOT.pth
wget http://www.robots.ox.ac.uk/~qwang/SiamMask_DAVIS.pth
```

### Run finder.py to mark the bounding box and to process the whole masking Run demo.py
### you can change your test data at cd data/tennis
### your masked image frames will be at tools/output_img


### Run demo.py
```
cd $SiamMask/experiments/siammask_sharp
export PYTHONPATH=$PWD:$PYTHONPATH
python ../../tools/demo.py --resume SiamMask_DAVIS.pth --config config_davis.json
```


## IL_video_inpainting
### We provide two ways to test our video inpainting approach. Please first download the demo data from here into data/ and download the pretrained model weights for PWC-Net from here (No need to unzip the weights file) into pretrained_models/. (The model was originally trained by Simon Niklaus from here).

### To run our demo, please run the following command:
```
python3 train.py --train_mode DIP-Vid-Flow --video_path data/bmx-trees.avi --mask_path data/bmx-trees_mask.avi --resize 192 384 --res_dir result/DIP_Vid_Flow
```

# Links:
### Youtube:https://youtu.be/5QCMeVwYcTA
### Linked in:https://www.linkedin.com/posts/karthikeyanthanigai_csebennett-leadingindiaai-activity-6615838390803886080-GSP_
