from bpyutils.matutils import createStandardMaterial
from numpy import linspace

def jet(val):
	"""
	
	"""
	rr = max(0,min(1,min(4*val-1.5, -4*val+4.5)))
	gg = max(0,min(1,min(4*val-0.5, -4*val+3.5)))
	bb = max(0,min(1,min(4*val+0.5, -4*val+2.5)))
	
	
	return (rr,gg,bb)

def submap(cmapfun=jet,startval=0.25,endval=0.75):
	"""
	
	"""
	return lambda x: cmapfun((x-startval)/(endval-startval))

def appendAlpha(rgb,alphaval=1):
	"""
	Utility function to add on the alpha channel to make a 4-tuple
	"""
	# Don't check that the input is the correct length, as we might want to repurpose this at some point
	
	return rgb + (alphaval,)

def colormapMaterials(cmapfun=jet,numMaterials=10,baseMaterial=None,nodeName='Diffuse BSDF',nodeInput=0):
	"""
	Taking a base material, create duplicates and change the colour
	according to the specified colourmap
	"""
	if baseMaterial is None:
		baseMaterial = createStandardMaterial((1,1,1))
	
	collist = [cmapfun(x) for x in linspace(0,1,numMaterials)]
	
	matlist = [baseMaterial.copy() for x in collist]
	
	for x,y in zip(matlist,collist):
		x.node_tree.nodes[nodeName].inputs[nodeInput].default_value = y + (1,)
	
	return matlist
	
	