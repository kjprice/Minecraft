from .fill_command import fill_command_from_sea_level


def fill_path(y = 0, x_start = 0, x_distance = 0, z_start = 0, z_distance = 0, block='stone', other_args=[]):
    x_end = x_start + x_distance
    z_end = z_start + z_distance

    return fill_command_from_sea_level(x1=x_start, y1=y, z1=z_start, x2=x_end, y2=y, z2=z_end, block=block, other_args=other_args)
