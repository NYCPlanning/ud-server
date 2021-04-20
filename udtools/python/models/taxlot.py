from shapely import wkt
from generated.site_pb2_grpc import SiteServiceStub
from connectors.postgis import prepare_parameterized_query
from geography.coordinate_systems import crs_nystateplane
import geopandas as gpd
from models.lot import Lot

def lots_by_bounds(conn, params):
  lots = []
  query_path = '../../core/python/connectors/queries/lots.sql'
  (query, bind_params) = prepare_parameterized_query(query_path, params)
  cursor = conn.cursor()
  cursor.execute(query, bind_params)

  for i, row in enumerate(cursor):
    geom = wkt.loads(row['geomwkt'])
    l = TaxLot(row['bbl'], geom)
    lots.append(l)

  return lots

class TaxLot(Lot):

  # old one, meant to be shapely geom object
  def __init__(self, bbl, geom):
    bbl_string = str(bbl)
    super(self.__class__, self).__init__(bbl_string, geom)
    self.bbl = bbl_string

  def say_hello(self):
    print('hi')
