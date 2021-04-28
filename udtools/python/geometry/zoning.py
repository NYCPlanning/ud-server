import math

from OCC.Core.gp import (
  gp_Pnt, 
  gp_Pnt2d, 
  gp_Vec, 
  gp_Dir, 
  gp_Ax1, 
  gp_Ax2, 
  gp_Pln, 
  gp_Trsf
)
from OCC.Core.Geom import Geom_Curve, Geom_OffsetCurve
from OCC.Core.TopLoc import TopLoc_Location

from geometry.brep import loft_wires
from geometry.conversion import curve_to_wire
from geometry.curve import fit_offset_to_bounds
from geometry.reference import world_pos_z

def build_yard_cutter(lotline, bounds, dims):
    """where dims is a 2d list specifying setbacks and elevations
       measured in absolute distance from the lot line"""
    wires = [curve_to_wire(lotline)]

    for i, d in enumerate(dims):
        print(f'curve {i+1}:')

        # handle setback
        # if d[0] > 0:
        setback_distance = d[0]
        setback_curve = Geom_OffsetCurve(
          lotline, 
          -setback_distance, 
          world_pos_z
        )
        setback_curve = fit_offset_to_bounds(
          setback_curve,
          bounds,
        )
        print(f'...set back by {setback_distance}')

        # handle elevation
        # if d[1] > 0:
        elevation_distance = d[1]
        setback_curve.Translate(gp_Vec(0, 0, elevation_distance))
        print(f'...elevated by {elevation_distance}')

        wires.append(curve_to_wire(setback_curve))

    # add one more curve to close at the top
    closure_elevation = dims[-1][1]
    movement = gp_Trsf()
    movement.SetTranslation(gp_Vec(0, 0, closure_elevation))
    location = TopLoc_Location(movement)
    closure_wire = wires[0].Moved(location)
    wires.append(closure_wire)

    return loft_wires(wires)
