class Tilemap:
  def __init__(self, tile_size =16):
    self.tile_size = tile_size
    self.tilemap = {}
    self.offgrid_tiles = []

    for i in range(10):
      self.tile[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
      self.tile['10' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    