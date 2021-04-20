from datetime import datetime

class Scenario():
  """A moment in time: past, present or any number of potential futures."""

  def __init__(self, id_):
    self.id_ = id_
    self.build_year = datetime.now().year

  def summarize(self):
    print('not yet implemented')
