from .fill_command import fill_command_from_sea_level
def build_around_player(distance=0, y_bottom=0, y_distance=0, x_offset=0, z_offset=0, block='air', other_args=[]):
  return fill_command_from_sea_level(
      x1=-distance + x_offset,
      x2=distance + x_offset,
      z1=-distance + z_offset,
      z2=distance + z_offset,
      y1=y_bottom,
      y2=y_distance +  y_bottom,
      block=block,
      other_args=other_args
      )
