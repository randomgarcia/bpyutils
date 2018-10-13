import bpy

def copyObject(obj,newlocation=None):
	obj2 = obj.copy()
	obj2.data = obj.data.copy()
	
	# link the object to the scene
	bpy.context.scene.object.link(obj2)
	
	if newlocation is not None:
		obj2.delta_location = newlocation
	
	return obj2
	
def setMaterial(obj,mat):
	"""
	Convenience function for assigning a material to an object
	"""
	if obj.data.materials:
		# assign to 1st material slot
		obj.data.materials[0] = mat
	else:
		# no slots
		obj.data.materials.append(mat)