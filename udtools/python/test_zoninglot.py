import pprint
#from OCC.Display.SimpleGui import init_display

from models.zoninglot import ZoningLot
from models.site import Site
from models.scenario import Scenario

pp = pprint.PrettyPrinter()

my_scenario = Scenario('A')
my_site = my_site = Site('1', ['2025770020', '2025770022'])
my_zoninglot = ZoningLot(my_scenario, my_site)

# pp.pprint(my_zoninglot.edges)
# pp.pprint(my_zoninglot.measure_frontage())
# pp.pprint(my_zoninglot.load_buildings())

# print(my_zoninglot.edges['front'][0]['geom'])
print(my_zoninglot.geom)

massing_goals = [
  {'height': 15.0, 'usegroup': 4, 'label': 'school'},
  {'height': 10.0, 'usegroup': 2, 'label': 'residential'},
]

envelope = my_zoninglot.generate_envelope(massing_goals)
building = my_zoninglot.generate_building(massing_goals)

# print(building.summarize())

print('done')