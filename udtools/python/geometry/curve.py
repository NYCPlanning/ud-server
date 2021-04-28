import copy
from OCC.Core.Geom import Geom_OffsetCurve
from OCC.Core.Geom2d import Geom2d_OffsetCurve
from OCC.Core.GeomAPI import GeomAPI_ProjectPointOnCurve
from OCC.Core.Geom2dAPI import Geom2dAPI_ProjectPointOnCurve
from geometry.conversion import coords_to_curve
from geometry.reference import world_pos_z

def fit_offset_to_bounds(offset, bounds):
  """extend/trim ends of 3d offset curve to meet 2d bounds curve"""
  pts = []

  for i, p in enumerate([offset.Value(0), offset.Value(1)]):
    offset_z = offset.Value(0.5).Z()
    p = GeomAPI_ProjectPointOnCurve(p, bounds).NearestPoint()
    pt = (p.X(), p.Y(), offset_z)
    pts.append(pt)

  return coords_to_curve(pts)


def offset(curve, distance):
  """offset 2d curve by distance, negative is in, positive out"""
  return Geom2d_OffsetCurve(curve, distance)


def lift(curve, distance):
  """offset curve in positive z direction by distance"""
  return Geom_OffsetCurve(curve, distance, world_pos_z)