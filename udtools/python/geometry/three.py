# from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
# from OCC.Core.IMeshTools import IMeshTools_Parameters
#from OCC.Core.RWGltf import RWGltf_CafWriter
# from OCC.Core.StlAPI import stlapi_Write, StlAPI_Writer
# import json
from OCC.Core.Tesselator import ShapeTesselator
import gzip

def serialize_shape(s):
  # mesh the shape
  # params = IMeshTools_Parameters()
  # params.Deflection = 0.01
  # params.Angle = 0.5
  # result = BRepMesh_IncrementalMesh(s, params)

  # compute the tessellation
  tess = ShapeTesselator(s)
  tess.Compute()

  # convert to threejs json
  three_json = tess.ExportShapeToThreejsJSONString('UDTools')
  b = bytes(three_json, 'utf-8')
  c = gzip.compress(b)
  return c
