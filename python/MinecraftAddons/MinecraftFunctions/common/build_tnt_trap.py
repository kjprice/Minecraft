from .fill_command import fill_command_from_sea_level

def build_tnt_trap(x1=0, y1=-1, z1=0, x2=0, y2=-1, z2=0):
    output = []
    output.append(fill_command_from_sea_level(x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2, block='tnt'))
    output.append(fill_command_from_sea_level(x1=x1, y1=y1+1, z1=z1, x2=x2, y2=y2+1, z2=z2, block='wooden_pressure_plate', other_args=['0']))
    return '\n'.join(output)
# build_tnt_trap()