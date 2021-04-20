from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static_SetCVal

def shape_to_step(shape, path): 
  step_writer = STEPControl_Writer()
  Interface_Static_SetCVal("write.step.schema", "AP203")
  Interface_Static_SetCVal("xstep.cascade.unit", "FT")
  step_writer.Transfer(shape, STEPControl_AsIs)
  status = step_writer.Write(path)
  return status
