# base class for zoning lot/tax lot
# don't use!
class Lot():

  def __init__(self, id_, geom):
      self.id_ = id_
      self.geom = geom

  def identify(self):
      print(f"my name is {self.id_}")
