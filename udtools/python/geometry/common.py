import re
import math
# from OCC.Core import GeomAPI
from OCC.Core.BOPAlgo import BOPAlgo_MakeConnected, BOPAlgo_BuilderSolid
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Common
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakePolygon, BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakeShell, BRepBuilderAPI_MakeSolid
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.gce import gce_MakePln
from OCC.Core.GeomAPI import GeomAPI_PointsToBSpline
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Ax2, gp_Pln
from OCC.Core.ShapeUpgrade import ShapeUpgrade_UnifySameDomain
from OCC.Core.TColgp import TColgp_Array1OfPnt
from OCC.Core.TColgp import TColgp_HArray1OfPnt2d, TColgp_Array1OfPnt2d
from OCC.Core.TopTools import TopTools_ListOfShape
from OCC.Display.WebGl.jupyter_renderer import JupyterRenderer
import OCC.Core.TColgp as tcol

# extrude vertically
def extrude_face(shape, distance):
  v = gp_Vec(0, 0, distance)
  result = BRepPrimAPI_MakePrism(shape, v)
  return result

# takes flat list of occ faces
# fuses together
# and returns result
def fuse_faces(faces):
    count = len(faces)
    n = 1
    result = BRepBuilderAPI_MakeFace()
    
    for face in faces:
        if n > count : break
    
        try:
          result = BRepAlgoAPI_Fuse(result.Shape(), face.Shape())
        except RuntimeError:
          result = face
            
        n += 1
    
    result = upgrade_brep(result.Shape())
    
    return result

# given a brep and an elevation in the z-axis,
# return a brep face representing the section at that level
def section_at(brep, elevation):
    positive_z = gp_Dir(0, 0, 1)
    origin = gp_Pnt(0, 0, elevation)
    pln = gp_Pln(origin, positive_z)
    pln_face = BRepBuilderAPI_MakeFace(pln).Shape()
    section = BRepAlgoAPI_Common(brep, pln_face)
    return section.Shape()

# function to return true or false if azimuth a
# is within 45 degrees of all values in a list of azimuth b
def within_45_all(az_a, list_of_az_b):
  tests = []

  for az_b in list_of_az_b:
    # test uses modulo to ignore direction of azimuth
    az_a_ignoredir = az_a % math.pi
    az_b_ignoredir = az_b % math.pi
    test = (az_b_ignoredir - math.pi/4) <= az_a_ignoredir <= (az_b_ignoredir + math.pi/4)
    tests.append(test)
       
  return all(tests)