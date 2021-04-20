from enum import Enum

# base class for existingbuilding/proposedbuilding
# don't use!
class Building():

  def __init__(self, id_, envelope):
    self.id_ = id_
    self.envelope = envelope

  def say_hello(self):
    print(f'hi I am {self.bin}')

  def to_three_json(self):
    return serialize_shape(self.envelope)

# defines a building's exterior volume, with tagged faces
class BuildingEnvelope():
  
  def __init__(self, brep):
    self.geom = brep
    self.face_tags = []

  def tag_faces(self):
    print('not implemented')

# for a given face of a brep, identified by index
# what kind of building surfae this is
class BuildingFace():

  def __init__(self, index, type):
    self.i = index
    self.type = BuildingFaceType.UNKNOWN

# available building face types
class BuildingFaceType(Enum):
    UNKNOWN = 0   # Unknown face type (default)
    ROOF = 1      # Roof
    LOTLINE = 2   # Lot line facade
    FRONT = 3     # Street-facing facade
    INTERIOR = 4  # Interior facade
    BELLY = 5     # Underside
