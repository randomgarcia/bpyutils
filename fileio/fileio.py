import csv
import os
#import bpy


def readcsv(fullpath):
    with open(fullpath, 'r', newline='') as csvfile:
        ofile = csv.reader(csvfile, delimiter=',')
        #next(ofile) # <-- skip the x,y,z header
        
        # this makes a generator of the remaining non-empty lines
        rows = (r for r in ofile if r)
        
        # this converts the string representation of each line
        # to an x,y,z list, and stores it in the verts list.
        verts = [[float(i) for i in r] for r in rows]
    
    return verts

