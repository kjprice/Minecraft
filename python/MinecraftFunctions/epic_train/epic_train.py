from ..minecraft_function.minecraft_function import MinecraftFunction
from ..common.fill_path import fill_path
from ..conf import SEA_LEVEL
# from ..common.reset_build import ResetBuild

def set_track(x = 0, y = 0, z = 0):
    y = SEA_LEVEL + y + 1
    return 'setblock ~{} {} ~{} rail'.format(x, y, z)

def create_track_path(y = 0, x_start = 0, x_distance = 0, z_start = 0, z_distance = 0):
    output = []

    output.append(fill_path(y=y, x_start=x_start, x_distance=x_distance, z_start=z_start, z_distance=z_distance, block='redstone_block'))
    output.append(fill_path(y=y + 1, x_start=x_start, x_distance=x_distance, z_start=z_start, z_distance=z_distance, block='golden_rail'))
    return '\n'.join(output)

DIRECTIONS = {
    'NORTH': [0, -1],
    'EAST': [1, 0],
    'SOUTH': [0, 1],
    'WEST': [-1, 0],
}

DEFAULT_POSITION = [0, 0, 0] # center - immutable

class EpicTrain(MinecraftFunction):
    track_position = None
    direction = None
    def __init__(self):
        self.track_position = DEFAULT_POSITION
        self.direction = [1, 0] # Facing East
        super().__init__('epic_train')
    
    def get_x_z_distance(self, direction, distance):
        blocks_to_create = distance - 1
        return list(map(lambda d: d * blocks_to_create, direction))
        
    # All tracks except the first need to start one block over from where the previous ended
    def get_starting_position(self, direction):
        if self.track_position is DEFAULT_POSITION:
            return self.track_position
        
        x, y, z = self.track_position
        starting_position = [
            x + direction[0],
            y,
            z + direction[1],
        ]
        
        return starting_position

    def set_turning_track(self, new_direction):
        if self.track_position is DEFAULT_POSITION:
            return
        if new_direction == self.direction:
            return
        
        x, y, z = self.track_position
        self.run(set_track(x=x, y=y, z=z))
    
    def go_with_incline(self, direction: DIRECTIONS, distance: int, inclineDirection):
        if not inclineDirection in [-1, 0, 1]:
            raise ValueError("Incline can only be magnitutde of 1, cannot accept {}".format(inclineDirection))
        if inclineDirection == 0:
            self.go(direction, distance)
            return
        
        if direction is not self.direction:
            raise Exception('Cannot change directions and change incline at the same time')

        for d in range(distance):
            self.go(direction, 1)
            if d != distance - 1:
                x, y, z = self.track_position
                self.track_position = [
                    x, y + inclineDirection, z
                ]

    def go(self, direction: DIRECTIONS, distance: int):
        x_start, y, z_start = self.get_starting_position(direction)
        x_distance, z_distance = self.get_x_z_distance(direction, distance)

        self.run(create_track_path(y = y, x_start = x_start, x_distance = x_distance, z_start = z_start, z_distance = z_distance))
        self.set_turning_track(direction)

        self.track_position = [
            x_start + x_distance,
            y,
            z_start + z_distance,
        ]
        self.direction = direction

    def goNorth(self, distance = 0, incline = 0):
        self.run('# North: {}'.format(distance))
        self.go_with_incline(DIRECTIONS['NORTH'], distance, incline)
    def goEast(self, distance = 0, incline = 0):
        self.run('# East: {}'.format(distance))
        self.go_with_incline(DIRECTIONS['EAST'], distance, incline)
    def goSouth(self, distance, incline = 0):
        self.run('# South: {}'.format(distance))
        self.go_with_incline(DIRECTIONS['SOUTH'], distance, incline)
    def goWest(self, distance = 0, incline = 0):
        self.run('# West: {}'.format(distance))
        self.go_with_incline(DIRECTIONS['WEST'], distance, incline)
    def build(self):
        self.run('# Building epic trains')
        
        self.run('tp @p ~ ~ ~ facing ~5 ~ ~') # Facing east
        self.run('function reset_build')
        self.run('kill @e[type=minecart]')

        self.run('setblock ~-1 ~ ~ stone')

        self.run('ride @p summon_ride minecart')
        self.goEast(2)
        self.goNorth(2)
        self.goWest(1)
        self.goWest(2, 1)


