from .fill_command import fill_command_from_sea_level
def build_empty_cube(x1=0, y1=0, z1=0, x2=0, y2=0, z2=0, block='stone'):
  wall_start_end_dimensions = {
      'wall_west': [[x1, y1, z1], [x1, y2, z2]],
      'wall_north': [[x1, y1, z1], [x2, y2, z1]],
      'wall_east': [[x2, y1, z1], [x2, y2, z2]],
      'wall_south': [[x1, y1, z2], [x2, y2, z2]],
      'floor': [[x1, y1, z1], [x2, y1, z2]],
      'ceiling': [[x1, y2, z1], [x2, y2, z2]],
  }

  output = []
 
  for wall in wall_start_end_dimensions.keys():
    start, end = wall_start_end_dimensions[wall]
    x1, y1, z1 = start
    x2, y2, z2 = end
    output.append(fill_command_from_sea_level(x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2, block=block))
  return '\n'.join(output)
