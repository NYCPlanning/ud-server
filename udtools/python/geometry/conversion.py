import re
import math
# from OCC.Core import GeomAPI
from OCC.Core.BOPAlgo import BOPAlgo_MakeConnected, BOPAlgo_BuilderSolid
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Common
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
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
import shapely.wkt

# takes a shapely coord_sequence as input (list of coordinate tuples)
# returns occ polygon
def shape_to_occ_polygon(shape, z=False):
  if shape.geom_type == 'Polygon': coords = shape.exterior.coords
  else: coords = shape.coords

  points = []
  
  if z: points = [ gp_Pnt(x, y, z) for (x, y, z) in coords ]
  else: points = [ gp_Pnt(x, y, 0) for (x, y) in coords ]
  
  polygon = BRepBuilderAPI_MakePolygon()
  for p in points:
      polygon.Add(p)
  return polygon.Shape()


def coords_to_array(coords):
  """Converts list of tuples representing points to OCC Array of OCC Point"""
  occ_array = TColgp_Array1OfPnt(1, len(coords))

  for i, p in enumerate(coords):
    occ_pt = gp_Pnt(*p)
    occ_array.SetValue(i + 1, occ_pt)

  return occ_array
  

def coords_to_curve(coords):
  """Converts list of tuples representing points to OCC Curve"""
  occ_array = coords_to_array(coords)
  occ_curve = GeomAPI_PointsToBSpline(occ_array, 1, 1).Curve()
  return occ_curve


def coords_to_polygon(coords):
  """Converts list of tuples representing points to OCC Polygon"""
  occ_polygon = BRepBuilderAPI_MakePolygon()
  
  for p in coords:
    occ_pt = gp_Pnt(*p)
    occ_polygon.Add(occ_pt)

  return occ_polygon.Shape()


def curve_to_face(curve):
  """Converts OCC Curve to OCC Face"""
  wire = curve_to_wire(curve)
  face = BRepBuilderAPI_MakeFace(wire).Shape()
  return face


def curve_to_wire(curve):
  """Converts OCC Curve to OCC Wire"""
  edge = BRepBuilderAPI_MakeEdge(curve).Shape()
  wire = BRepBuilderAPI_MakeWire(edge).Shape()
  return wire


# takes a shapely multipolygon as input
# (ignores holes)
# returns list of occ faces
def multipolygon_to_faces(shape):
    faces = []
    #wires = []

    shapely_polygons = shape.geoms
    
    for p in shapely_polygons:
        occ_polygon = coords_to_polygon(p.exterior.coords)
        wire = occ_polygon.Wire()
        face = BRepBuilderAPI_MakeFace(wire, True)
        faces.append(face)
        # to get wire it would be 
        # occ_polygon.Wire()
        
    return faces


def polyhedralsurfacez_to_brep(wkt):
    occ_faces = TopTools_ListOfShape()
        
    outer_regex = r'(POLYHEDRALSURFACE Z \()([\(\)\d\.\,\-\s\(]*\))(\))'
    inner_regex = r'\(([\d\.\,\s\-]*)\)'
    
    body = re.search(outer_regex, wkt).group(2)
    faces = re.findall(inner_regex, body)
    
    for f in faces:
        face_coords = []
        # var coordinatepairlist = p.Replace(")", "").Replace("(", "").Split(',');
        f_clean = f.replace(')', '').replace(')', '')
        f_split = f_clean.split(',')
        for pt in f_split:
            coords = [float(d) for d in pt.split(' ')]
            face_coords.append(tuple(coords))
        
        face_polygon = coords_to_polygon(face_coords, z=True)
        face = BRepBuilderAPI_MakeFace(face_polygon.Wire(), True)
        face = BRepBuilderAPI_MakeFace(face_polygon.Wire(), True)
        occ_faces.Append(face.Shape())
    
    # weld faces into solid
    make_solid = BOPAlgo_BuilderSolid()
    make_solid.SetShapes(occ_faces)
    make_solid.Perform()
    
    # weld faces together
#     make_connected = BOPAlgo_MakeConnected()
#     make_connected.SetArguments(occ_faces)
#     make_connected.Perform()
    
#     result = upgrade_brep(make_connected.Shape())
#     return result

    return make_solid

def wire_to_face(wire):
  """OCC Wire to OCC Face"""
  face = BRepBuilderAPI_MakeFace(wire, True)
  return face.Shape()

def wkt_to_occ(wkt):
  shape = shapely.wkt.loads(wkt)

  handlers = {
    # 'Point': print,
    'LineString': shape_to_occ_polygon,
    # 'Multi': print,
    'Polygon': shape_to_occ_polygon,
    'MultiPolygon': print,
    # shapely doesn't handle 3d (polyhedralsurface z)
  }

  handler = handlers.get(shape.geom_type, lambda: "Not supported")
  result = handler(shape)
  return result
