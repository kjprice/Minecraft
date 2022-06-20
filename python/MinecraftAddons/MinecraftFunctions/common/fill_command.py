from ..conf import CMD_TEMPLATE_FULL_RELATIVE, CMD_TEMPLATE_FULL_ABSOLUTE, SEA_LEVEL

def fill_command(x1="", y1="", z1="", x2="", y2="", z2="", block="stone", other_args=[]):
  return CMD_TEMPLATE_FULL_RELATIVE.format(x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2, block=block, other=" ".join(other_args))

def fill_command_from_sea_level(x1="", y1=0, z1="", x2="", y2=0, z2="", block="stone", other_args=[]):
  y1 = y1 + SEA_LEVEL
  y2 = y2 + SEA_LEVEL
  return CMD_TEMPLATE_FULL_ABSOLUTE.format(x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2, block=block, other=" ".join(other_args))
