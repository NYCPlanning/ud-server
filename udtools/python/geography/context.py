import shapely.wkt as wkt

# get the nearest street on the city map
def nearest_street(start_pt, direction):
  print('not implemented')

def zone_by_context(pt):
  print('not implemented')

def base_plane_elevation(pt):
  print('not implemented')

aoi_default_wkt = '''POLYGON ((1009405.90154069 234515.39897036, 1009930.58999844 234367.63467916, 1009849.1944143 234052.07026066, 1009314.48803851 234194.82559284, 1009405.90154069 234515.39897036))'''

aoi_default = wkt.loads(aoi_default_wkt)

# next, specify bbls
bbl_array = ['2025770020', '2025770022']
