#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:39:16 2021

@author: sst
"""
import os,glob
import numpy as np
import time
from time import sleep
from shutil import copyfile

datasetDir = '/media/sst/Disk 3/timesets'

for setType in ['train','test']:

    for dataSize in [256,512,1024]:
        
        newDir = datasetDir + '/' + setType + '/' + str(dataSize) + '_1'
        if not os.path.isdir(newDir):
                os.mkdir(newDir)
                os.mkdir(os.path.join(newDir, 'labels'))
                os.mkdir(os.path.join(newDir, 'images'))
        txtDir = datasetDir + '/' + setType + '/' + str(dataSize) +'/labels'
        
        for file in sorted(glob.glob(os.path.join(datasetDir + '/' + setType + '/' + str(dataSize) +'/images','*.npy'))):
            _,frameNoStr = os.path.split(file)
            aa=np.load(file)
            img = aa.transpose(1,2,3,0).reshape(-1,aa.shape[2],aa.shape[3])
            np.save(os.path.join(newDir,'images', frameNoStr),img)
            copyfile(os.path.join(txtDir,frameNoStr[0:-4] +'.txt'),os.path.join(newDir, 'labels', frameNoStr[0:-4] +'.txt'))
            os.remove(file)     
