from pyproj import CRS, Proj, Transformer

crs_wgs84 = CRS('EPSG:4326')
crs_webmercator = CRS('EPSG:3857')
crs_nystateplane = CRS('EPSG:2263')

wgs84_to_nystateplane = Transformer.from_crs(
    crs_wgs84, 
    crs_nystateplane, 
    always_xy=True
  ).transform

point_nycityhall_wgs84 = [
  40.71273670544531,
   -74.00600376511792
]

test_studyarea_wgs84 = 'POLYGON ((-73.993996 40.67882, -73.99328800000001 40.67847, -73.993723 40.677831, -73.994533 40.678238, -73.993996 40.67882))'