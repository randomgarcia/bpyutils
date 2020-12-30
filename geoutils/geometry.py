import math
import bpy
import bpyutils.fileio as fileio

#pasted from:
# https://blender.stackexchange.com/questions/5898/how-can-i-create-a-cylinder-linking-two-points-with-python
def cylinder_between(x1, y1, z1, x2, y2, z2, r):

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1    
    dist = math.sqrt(dx**2 + dy**2 + dz**2)
    
    bpy.ops.mesh.primitive_cylinder_add(radius = r, depth = dist, location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)) 
    
    phi = math.atan2(dy, dx)
    theta = math.acos(dz/dist) 
    
    bpy.context.object.rotation_euler[1] = theta 
    bpy.context.object.rotation_euler[2] = phi 

def lineScale(x1,y1,z1,x2,y2,z2,scale):
    """
    
    """
    halfscale = 0.5*(scale - 1) + 1
    
    x2a = halfscale*(x2-x1) + x1
    x1a = halfscale*(x1-x2) + x2
    
    y2a = halfscale*(y2-y1) + y1
    y1a = halfscale*(y1-y2) + y2
    
    z2a = halfscale*(z2-z1) + z1
    z1a = halfscale*(z1-z2) + z2
    
    return x1a,y1a,z1a,x2a,y2a,z2a
    
    
def lineDelta(x1,y1,z1,x2,y2,z2,delta):
    """
    
    """
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1    
    dist = math.sqrt(dx**2 + dy**2 + dz**2)
    
    halfscale = 1 + delta/dist
    
    x2a = halfscale*(x2-x1) + x1
    x1a = halfscale*(x1-x2) + x2
    
    y2a = halfscale*(y2-y1) + y1
    y1a = halfscale*(y1-y2) + y2
    
    z2a = halfscale*(z2-z1) + z1
    z1a = halfscale*(z1-z2) + z2
    
    return x1a,y1a,z1a,x2a,y2a,z2a
    

def delaunayCylinders(vertfile,edgefile,rr=0.1,delta=-0.05):
    """
    
    """
    verts = fileio.readcsv(vertfile)
    edges = fileio.readcsv(edgefile)
    
    for edge0 in edges:
        v1 = verts[int(edge0[0])]
        v2 = verts[int(edge0[1])]
        
        x0,y0,z0,x1,y1,z1 = lineDelta(v1[0],v1[1],v1[2],v2[0],v2[1],v2[2],delta)
        
        cylinder_between(x0,y0,z0,x1,y1,z1,rr)
    
    