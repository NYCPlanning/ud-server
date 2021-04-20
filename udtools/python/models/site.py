class Site:
  """A geographic location, for now defined as a list of NYC tax lot BBL identifiers."""

  def __init__(self, id_, taxlot_ids):
    self.id_ = id_
    self.taxlot_ids = taxlot_ids
