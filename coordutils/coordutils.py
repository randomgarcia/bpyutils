# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:13:04 2019

@author: Adam
"""

from bpyutils.fileio import readcsv

import math
import numpy as np

def rotationMatrix(alpha,beta,gam):
    
    r1 = np.array([[1,0,0],[0,math.cos(gam),-math.sin(gam)],[0,math.sin(gam),math.cos(gam)]])
    r2 = np.array([[math.cos(beta),0,math.sin(beta)],[0,1,0],[-math.sin(beta),0,math.cos(beta)]])
    r3 = np.array([[math.cos(alpha),-math.sin(alpha),0],[math.sin(alpha),math.cos(alpha),0],[0,0,1]])
    
    r12 = np.matmul(r1,r2)
    rmat = np.matmul(r12,r3)
    
    return rmat


