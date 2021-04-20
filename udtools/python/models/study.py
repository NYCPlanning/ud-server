from models.zoninglot import MassingGoals

class Study():

  def __init__(self, id_):
    self.id_ = id_
    self.scenarios = []
    self.sites = []
    self.zoninglots = []
    self.proposedbuildings = []
    self.massing_goals = MassingGoals([15, 10], [2], [])

  def add_scenario(self, scenario):
    print('not implemented')
  
  def add_site(self, site):
    print('not implemented')

  def add_custom_zone(self, zone):
    print('not implemented')

  def summarize(self):
    print('not implemented')
