from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakePolygon
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_ThruSections
from OCC.Core.ShapeUpgrade import ShapeUpgrade_UnifySameDomain
from geometry.conversion import curve_to_wire

def loft_wires(wires, closed=True):
  """From a list of OCC Wires, build up a solid by lofting"""
  loft = BRepOffsetAPI_ThruSections(True, True, 0.1)

  # end caps
  # wire_sp = BRepBuilderAPI_MakePolygon()
  # wire_ep = BRepBuilderAPI_MakePolygon()

  if closed: wires.append(wires[0])

  for w in wires:
    loft.AddWire(w)

  return loft.Shape()

def upgrade(brep):
  """use SetAngularTolerance(), SetLinearTolerance() to fine-tune results"""
  result = ShapeUpgrade_UnifySameDomain(brep, True, True, False)
  result.SetAngularTolerance(0.1)
  result.SetLinearTolerance(0.1)
  result.Build()
  return result.Shape()
