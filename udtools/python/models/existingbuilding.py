from connectors.postgis import prepare_parameterized_query
from generated.site_pb2_grpc import SiteServiceStub
from geometry.common import polyhedralsurfacez_to_brep
from geometry.three import serialize_shape
from models.building import Building

# gets a list of new building objects from the database
def existing_buildings_by_bounds(conn, params):
  bldgs = []
  query_path = '../../core/python/connectors/queries/buildings.sql'
  (query, bind_params) = prepare_parameterized_query(query_path, params)
  cursor = conn.cursor()
  cursor.execute(query, bind_params)

  for row in cursor:
    brep_geom = polyhedralsurfacez_to_brep(row['geomwkt'])
    brep = brep_geom.Areas().First() # if valid, will result in one solid
    b = ExistingBuilding(row['bin'], brep)
    bldgs.append(b)

  return bldgs

class ExistingBuilding(Building):

  def to_proposed_building():
    print('not implemented')

  def get_dob_records():
    print('not implemented')
