# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:03:38 2018

@author: Amr Amer
"""

import pydicom
from scipy.misc import imresize
import numpy as np
import os

fold = "/home/ishwar/project/dataset/HGG"

#folders_for_today = ['HF1264', 'HF1316', 'HF1325', 'HF1334', 'HF1344', 'HF1345', 'HF1381',
#                     'HF1407', 'HF1433', 'HF1442', 'HF1463', 'HF1489', 'HF1511', 'HF1551',
#                     'HF1553', 'HF1568', 'HF1588', 'HF1606', 'HF1677', 'HF1708']
 
folderlist = os.listdir(fold)

folders_for_today = folderlist

for fldr in folderlist:
    
    if(fldr in folders_for_today):    
        loc = os.path.join(fold, fldr)
        print(loc)
    
        filelist = [os.path.join(loc, fl) for fl in os.listdir(loc)]
        os.mkdir(os.path.join(loc, "converted"))
        dest = [os.path.join(loc, "converted/", fl) for fl in os.listdir(loc)]
        
        for i,fl in enumerate(filelist):
            ds = pydicom.dcmread(fl)
            print(fl)
            im2 = imresize(ds.pixel_array,size=(240,240))
            im2 = im2.astype(np.uint16)
            ds.Rows,ds.Columns = im2.shape
            ds.PixelData = im2.tobytes()
            ds.save_as(dest[i])