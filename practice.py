from assets import bcolors
class tile:
    def __init__(self, title, char_input, color_code):
        self.title = title
        self.char_input = char_input
        self.color_code = color_code
        self.tile_char_type = "\033[{}m {}\033[00m".format(color_code, char_input)

    def tile_char(self):
        return self.char_input


hero_location = (0, 0)


def move_hero(x_inc, y_inc):
    old_loc = hero_location
    new_loc =(old_loc[0] + x_inc, old_loc[1] + y_inc)
    level_map[old_loc] = floor_tile
    level_map[new_loc] = hero_tile



floor_tile = tile("floor", "#", '91')
hero_tile = tile("hero", "*", '96')
void_tile = tile("void", " ", '98')


level_map = {(0, 2): floor_tile, (-1, 1): floor_tile, (0, 1): floor_tile, (1, 1): floor_tile, (-2, 0): floor_tile,
             (-1, 0): floor_tile, (0, 0): floor_tile, (1, 0): floor_tile, (2, 0): floor_tile, (-1, -1): floor_tile,
             (0, -1): floor_tile, (1, -1): floor_tile, (0, -2): floor_tile}


level_map[hero_location] = hero_tile


def move_hero(x_inc, y_inc):
    old_loc = hero_location
    new_loc =(old_loc[0] + x_inc, old_loc[1] + y_inc)
    level_map[old_loc] = floor_tile
    level_map[new_loc] = hero_tile


continue_loop = True
while continue_loop:
    for y in range(-2, 3):
        line = []
        output_line = []
        for x in range(-2, 3):
            if (x, y) in level_map.keys():
                tile = level_map[(x,y)]
                line.append(tile.tile_char())

        output_line = "\033[{}m {:^10}\033[00m".format("91", ''.join(line))                                                          #"{:^10}".format(''.join(line))
        print(output_line)
    cmd = input("What would you like to do?: ")

    #TODO dictionary use here
    if cmd.lower().strip() == "q" or cmd.lower().strip() == "quit":
        print("Quiting Gracefully")
        continue_loop = False

    elif cmd.lower().strip() == 'n':
        move_hero(0, -1)
    elif cmd.lower().strip() == 's':
        move_hero(0, 1)
    elif cmd.lower().strip() == 'e':
        move_hero(1, 0)
    elif cmd.lower().strip() == 'w':
        move_hero(-1, 0)


