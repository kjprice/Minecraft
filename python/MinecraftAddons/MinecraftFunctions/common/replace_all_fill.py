from .build_around_player import build_around_player
def replace_all_fill(x_distance=50, y_bottom=0, y_top=30, replace_from='water', replace_to='air'):
    output = []
    output.append('# Replacing {} with {}'.format(replace_from, replace_to))
    for i in range(y_bottom, y_top):
        output.append(build_around_player(x_distance, i, 0, block='air', other_args=['1', 'replace', replace_from]))
    return '\n'.join(reversed(output))
