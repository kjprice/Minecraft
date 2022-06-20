# from python.config_file import MIN_Y, MAX_Y
# import python.config_file
# from common.config_file  import MIN_Y, MAX_Y
# import ..conf
from ..conf import MIN_Y, MAX_Y
# Huge triangle stairs
def build_triangle_stairs():
  for x, y2 in enumerate(range(MIN_Y, MAX_Y)):
    CMD_TEMPLATE_2 = "fill ~{x1} {y1} ~{z1} ~{x2} {y2} ~{z2} {block}"
    print(CMD_TEMPLATE_2.format(x1=x, y1=MIN_Y, z1="", x2=x, y2=y2, z2="", block="stone"))
