import bpy
from mathutils import Vector

"""
	if ob.data.materials:
		# assign to 1st material slot
		ob.data.materials[0] = mat
	else:
		# no slots
		ob.data.materials.append(mat)
"""

def setDiffuseNodeColor(obj,color):
	if type(obj) is bpy.types.Object:
		mat = obj.data.materials[0]
	else:
		# should be a material already
		mat = obj
	
	diffusenode = mat.node_tree.nodes.get('Diffuse BSDF')
	# for now, assume that there'll only be one
	
	if len(color)==3:
		alpha = diffusenode.inputs[0].default_value[3]
		color = tuple(color) + (alpha,)
	
	diffusenode.inputs[0].default_value = color

def setNodeColor(obj,color,nodename=None):
	if nodename is None:
		nodename = 'Diffuse BSDF'
	
	if type(obj) is bpy.types.Object:
		mat = obj.data.materials[0]
	else:
		# should be a material already
		mat = obj
	
	diffusenode = mat.node_tree.nodes.get(nodename)
	# for now, assume that there'll only be one
	
	if len(color)==3:
		alpha = diffusenode.inputs[0].default_value[3]
		color = tuple(color) + (alpha,)
	
	diffusenode.inputs[0].default_value = color


def createStandardMaterial(drgb,grough=0.2,factor=0.2,name='Standard Material',grgb=(1,1,1,1),drough=0):
	"""
	Go through the process to make the standard
	glossy and diffuse mix shader
	"""
	mat = bpy.data.materials.new(name)
	mat.use_nodes = True
	
	if len(drgb)<4:
		drgb+=(1,)
	
	if len(grgb)<4:
		grgb+=(1,)
	
	nodes = mat.node_tree.nodes
	
	# should already have the diffuse node and the output node
	diffusenode = nodes['Diffuse BSDF']
	outputnode = nodes['Material Output']
	
	mixnode = nodes.new('ShaderNodeMixShader')
	glossynode = nodes.new('ShaderNodeBsdfGlossy')
	
	# then sort out the connections
	links = mat.node_tree.links
	links.clear()
	links.new(diffusenode.outputs['BSDF'],mixnode.inputs[1])
	links.new(glossynode.outputs['BSDF'],mixnode.inputs[2])
	links.new(mixnode.outputs[0],outputnode.inputs['Surface'])
	
	# sort out the values
	mixnode.inputs[0].default_value = factor
	diffusenode.inputs[0].default_value = drgb
	diffusenode.inputs[1].default_value = drough
	glossynode.inputs[0].default_value = grgb
	glossynode.inputs[1].default_value = grough
	
	# set default locations so that the connections are clear
	diffusenode.location = Vector((-60,270))
	glossynode.location = Vector((-60,140))
	mixnode.location = Vector((130,230))
	outputnode.location = Vector((300,215))
	
	
	return mat
	
	