#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 16:08:05 2021

@author: aybora
"""

import os,glob
import numpy as np
from shutil import copyfile


multiFrameDir = "/media/aybora/SST/data/smolset/labels"

for dataSize in [256,512,1024]:

	featureDir = "/media/aybora/DATA/features/" + str(dataSize)
	destinationDir = "/media/aybora/DATA/timesets/" + str(dataSize)

	for file in sorted(glob.glob(os.path.join(multiFrameDir,'*.txt'))):
	    _,frameNoStr = os.path.split(file)
	    frameNo = int(frameNoStr[0:-4])
	    feat1 = np.load(os.path.join(featureDir,str(frameNo-1) + '.npy'))
	    feat2 = np.load(os.path.join(featureDir,str(frameNo) + '.npy'))
	    feat3 = np.load(os.path.join(featureDir,str(frameNo+1) + '.npy'))
	    featConc = np.concatenate((feat1,feat2,feat3))
	    np.save(os.path.join(destinationDir, str(frameNo)+'.npy'), featConc)
	    copyfile(file,os.path.join(destinationDir, str(frameNo) +'.txt'))
    
