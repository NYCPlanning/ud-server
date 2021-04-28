from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Pln

world_origin = gp_Pnt(0, 0, 0)
world_pos_z = gp_Dir(0, 0, 1)
world_xy = gp_Pln(world_origin, world_pos_z)
