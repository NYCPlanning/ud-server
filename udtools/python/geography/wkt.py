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