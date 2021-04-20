from models.building import Building
from geometry.measure import surface_area

class ProposedBuilding(Building):

  def __init__(self, floors):
    self.floors = floors

  def summarize(self):
    total = 0
    for floor in self.floors:
      total += surface_area(floor)
    print(f'{total} sqft in the current building')


class BuildingStorey():

  def __init__(self, level, geom, use):
    self.level = level # 0-indexed floor above ground
    self.geom = geom   # surface geometry of the floor
    self.use = use     # use definition
