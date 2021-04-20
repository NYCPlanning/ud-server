from enum import Enum
from connectors.postgis import run_query
from queries.zoninglot_shape import template as shape_template
from queries.zoninglot_edges import template as edges_template
from queries.zoninglot_buildings import template as buildings_template
from geography.context import aoi_default as aoi
from geometry.common import within_45_all, extrude_face, section_at, upgrade_brep
from geometry.conversion import wkt_to_occ, wire_to_face
from models.lot import Lot
from models.proposedbuilding import ProposedBuilding


class ZoningLot(Lot):
  """Represents a snapshot of a building Site at a particular moment in time (Scenario). Given a set of conditions (Zones) represents constraints and potentials needed to generate ZoningEnvelope and resultant ProposedBuilding objects."""

  def __init__(self, scenario, site):
    auto_id = f'{site.id_}_{scenario.id_}'
    super(self.__class__, self).__init__(auto_id, None) # inherits id_, geom
    self.area = None
    self.base_plane_elevation = 0
    self.buildings = []
    self.edges = []
    self.envelope = None
    self.scenario = scenario
    self.site = site
    self.type = None
    self.zones = []

    self.load_shape()
    self.load_edges()


  def calc_available_zfa(self):
    """Determines available ZFA by use given zones and lot area."""
    return None


  def define_zones(self):
    """Add zone definitions used to evaluate envelopes + buildings."""


  def generate_envelope(self, massing_goals):
    """Generates a new zoning envelope."""
    wire = wkt_to_occ(self.geom)
    face = wire_to_face(wire)
    prism = extrude_face(face, 100).Shape()
    prism = upgrade_brep(prism).Shape()
    self.envelope = prism
    return prism


  def generate_building(self, massing_goals):
    """Generates a proposed building."""
    floors = []
    # envelope = self.generate_envelope()
    for elev in [15, 25, 35, 45]:
        floor = section_at(self.envelope, elev)
        floors.append(floor)
    bldg = ProposedBuilding(floors)
    return bldg


  def load_shape(self):
    """Get shape of zoning lot from constituent tax lots from database."""
    params = {
      'center_x': aoi.representative_point().x,
      'center_y': aoi.representative_point().y,
      'bbl_array': self.site.taxlot_ids
    }
    result = run_query(shape_template, params)[0] # expect one item

    for k, v in zip(result._fields, result):
      setattr(self, k, v)


  def load_edges(self):
    """Get detailed lot edge information from database."""
    edge_ids = self.edges

    params = {
      'center_x': aoi.representative_point().x,
      'center_y': aoi.representative_point().y,
      'edge_array': edge_ids
    }
    results = run_query(edges_template, params)

    self.edges = {
      'ids': edge_ids,
      'front': [],
      'rear': [],
      'side': [],
    }

    results.sort(key=lambda i: i.front, reverse=True)
    for edge in results:
      e = edge._asdict()
      if edge.front: self.edges['front'].append(e)
      elif within_45_all(edge.azimuth, [fe['azimuth'] for fe in self.edges['front']]): self.edges['rear'].append(e)
      else: self.edges['side'].append(e)


  def load_buildings(self):
    """Get existing buildings on the zoning lot."""
    params = {
      'center_x': aoi.representative_point().x,
      'center_y': aoi.representative_point().y,
      'bldg_array': self.buildings,
      'edge_array': self.edges['ids'],
    }
    results = run_query(buildings_template, params)
    return results


  def measure_frontage(self):
    """Determine total length of street frontage."""
    return sum( [e['length'] for e in self.edges['front'] ] )


# along with a zoning lot, used to generate zoning envelope
class MassingGoals():

  def __init__(self, heights, uses, use_labels):
    self.heights = heights
    self.usegroups = uses
    self.labels = use_labels

# class ZoningEnvelope():

# what type of lotline is this
class LotEdge():

  def __init__(self, index, type):
    self.i = index
    self.type = LotLineType.UNKNOWN

# available lot line types
class LotLineType(Enum):
    UNKNOWN = 0 # unknown or default
    FRONT = 1
    SIDE = 2
    REAR = 3
