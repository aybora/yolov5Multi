#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:55:17 2021

@author: sst
"""
import os,glob
import numpy as np
import time
from time import sleep
from shutil import copyfile
from pathlib import Path

for dataset in ["train","test"]:  

    datasetDir = '/media/sst/Disk 1/timesets/'+ dataset
    
    for file in sorted(glob.glob(os.path.join(datasetDir, '256/images','*.npy'))):
        _,fileName = os.path.split(file)
        
        a256 = np.load(datasetDir+'/256/images/' + fileName)
        a512 = np.load(datasetDir+'/512/images/' + fileName)
        a1024 = np.load(datasetDir+'/1024/images/' + fileName)
        
        allres=np.concatenate((a256.reshape(-1),a512.reshape(-1),a1024.reshape(-1)))
        
        np.save(datasetDir+'/all/images/' + fileName, allres)
        
        copyfile(datasetDir + '/256/labels/'+ fileName[0:-4] + '.txt', datasetDir + '/all/labels/' + fileName[0:-4] + '.txt')
        
        os.remove(datasetDir+'/256/images/' + fileName)
        os.remove(datasetDir+'/512/images/' + fileName)
        os.remove(datasetDir+'/1024/images/' + fileName)