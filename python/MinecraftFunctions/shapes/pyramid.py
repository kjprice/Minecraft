from ..common.fill_command import fill_command
# Pyramid
def build_pyramid(y_bottom, y_top):
  y_points_reversed = list(range(y_bottom, y_top))[::-1]
  output = []
  for x_diff, y in enumerate(y_points_reversed):
    output.append(fill_command(
        x1=-(1 + x_diff),
        x2=(1 + x_diff),
        y1=y,
        y2=y,
        z1=-(1 + x_diff),
        z2=(1 + x_diff),
        block="stone"
                 ))
    return '\n'.join(output)

# build_pyramid(0, 90)
