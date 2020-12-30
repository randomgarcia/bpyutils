import bpy

from bpyutils.fileio import readcsv

import math
import numpy as np
import os

def placeObjects(coords,objmeth=None,coordscale=None,objscale=None):

    if type(coords) is str:
        coords = np.loadtxt(coords)

    if objmeth is None:
        objmeth = bpy.ops.mesh.primitive_uv_sphere_add

    if type(objmeth) is str:
        if objmeth.lower()=='cube':
            objmeth = bpy.ops.mesh.primitive_cube_add
        elif objmeth.lower()=='sphere':
            objmeth = bpy.ops.mesh.primitive_uv_sphere_add


    objlist = []

    if coordscale is not None:
        if type(coordscale) is not np.ndarray:
            coordscale = np.array(coordscale)
        coords = coords * coordscale

    for cc0 in coords:

        cc = list(cc0)

        if len(cc)<3:
            cc+=[0]

        objmeth(location=[x for x in cc])

        # need to work out how to scale the object first
        # do scaling here

        objlist.append(bpy.context.object)

    return objlist

def copyObject(obj,newlocation=None):
	obj2 = obj.copy()
	obj2.data = obj.data.copy()

	# link the object to the scene
	bpy.context.scene.objects.link(obj2)

	if newlocation is not None:
		obj2.delta_location = newlocation

	return obj2

def setMaterial(obj=None,mat=None):
	"""
	Convenience function for assigning a material to an object
	"""

	if obj is None:
		obj = bpy.context.object
	if obj.data.materials:
		# assign to 1st material slot
		obj.data.materials[0] = mat
	else:
		# no slots
		obj.data.materials.append(mat)


def imageCube(imagepath=None,position=(0,0,0),initialorientation='x'):
    """
    May need to reorient, as different blender installations seem to insert the
    planes with different orientations
    """

    # first parse the image path into folder and basename

    bpy.ops.import_image.to_plane(files=[{'name':imagepath}])
    obj0 = bpy.context.object

    obj0.location = position
    obj0.location.x = obj0.location.x - 0.5
    obj1 = copyObject(obj0,newlocation=(1,0,0))
    obj0.rotation_euler = (0,math.pi/2,0)
    obj1.rotation_euler = (0,-math.pi/2,0)


    obj2 = copyObject(obj0,newlocation=(0.5,-0.5,0))
    obj3 = copyObject(obj0,newlocation=(0.5,0.5,0))
    obj2.rotation_euler = (math.pi/2,0,0)
    obj3.rotation_euler = (-math.pi/2,0,0)


    obj4 = copyObject(obj0,newlocation=(0.5,0,0.5))
    obj5 = copyObject(obj0,newlocation=(0.5,0,-0.5))
    obj4.rotation_euler = (0,0,0)
    obj5.rotation_euler = (0,-math.pi,0)
