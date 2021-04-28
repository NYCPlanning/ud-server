from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakePolygon
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_ThruSections
from geometry.conversion import curve_to_wire

def loft_curves(curves, closed=True):
  """From a list of OCC Curves, build up a solid by lofting"""

  # the body of the loft
  loft = BRepOffsetAPI_ThruSections(True, True, 0.1)

  # end caps
  # wire_sp = BRepBuilderAPI_MakePolygon()
  # wire_ep = BRepBuilderAPI_MakePolygon()

  if closed: curves.append(curves[0])

  for c in curves:
      # wire_sp.Add(c.Value(0))
      # wire_ep.Add(c.Value(1))
      w = curve_to_wire(c)
      loft.AddWire(w)

  # shell = BRepBuilderAPI_MakeShell()
  # BRepBuilderAPI_MakeFace()
  # solid = BRepBuilderAPI_MakeSolid()

  return loft.Shape()
