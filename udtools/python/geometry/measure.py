from OCC.Core.BRepGProp import brepgprop_SurfaceProperties
from OCC.Core.GProp import GProp_GProps

def surface_area(shape):
  props = GProp_GProps()
  result = brepgprop_SurfaceProperties(shape, props)
  return props.Mass() # area is given as Mass for a surface
