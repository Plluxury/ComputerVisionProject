#This project create for object recognition
## To assemble it u will be need:
###1) Python 3.7.2
###2) libs that described in requirements.txt
###3) Debian 9 

## if u have python-opencv forever load problem u can fix it with command:

    pip install --upgrade pip setuptools wheel

## if u have libgl1 problem u can fix it with command:

    apt-get update && apt-get install libgl1

#About project

##1)CreateModel.py 
    Needs to create ur own model 
##2)ConvertVideo2Frames.py
    Needs to open video from which u want recognize objects
##3)VideoObjectDetectionMain.py
    Needs to detect objects on video

##4)Model.rar
    My data to create model that i use in this project
    P.S.  The labelImg module was used to create the data
    P.S.2 When u use labelImg, after select area you need to name it, 
          as you would like the area to be called when recognizing.
          All areas need to be name the same label.
          



https://wiki.nntc.nnov.ru/index.php?title=Docker
