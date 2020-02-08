#!/usr/bin/python
import os, shutil
from PIL import Image

#VARIABLES
data = {}

#Use input file for variables
def in_file():
    with open('path_to_variables_file', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            data[key] = value

    return data

#Copy directories to new location
def copy_dir():
    src = data['SRC']
    dest = data['DEST']
    destination = shutil.copytree(src,dest)
    print("Files have been copied to the new directory")

#Change the image format
def conv_img():
    for dirName, subdirList, fileList in os.walk(data['DEST']):
        for file in fileList:
            full_file_path = os.path.join(dirName, file)
            if file.endswith((".jpg") or (".JPG")):
                outfile = file[:-3] + data['IMGTYPE']
                im = Image.open(file)

                print ("new filename : " + outfile)
                im.save(os.path.join(dirName, outfile))

#Scale the image by 50%
#Set dpi to 150
#Message to say its complete

in_file()
copy_dir()
conv_img()
