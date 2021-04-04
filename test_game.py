import inspect
from assets import bcolors, HeroToken, TileToken
from map import load_map, map_tile_points, map_canvas_points


def is_quit(user_input):
    if user_input == 'q' or user_input == 'quit':
        return True
    else:
        return False


def draw_map(canvas_x, canvas_y, map_tiles):
    x_values = canvas_x // 2
    y_values = canvas_y // 2
    canvas = map_tiles

    for y in range(y_values, -y_values - 1, -1):
        for x in range(-x_values, x_values + 1):
            tile = canvas[(x, y)]
            if ((x + 1) * 2) < canvas_x:
                print("\033[{}m{} \033[00m".format(tile.color_code, tile.char), end=" ")
            else:
                print("\033[{}m{} \n\033[00m".format(tile.color_code, tile.char), end="")
                print()

alive = True
if __name__ == '__main__':
    while alive is True:
        hero_location = (0, 0)
        hero = HeroToken("*", "96", "Hero of Tolm")
        updated_map = load_map(13, 13, 5) # updates map
        updated_map[hero_location] = hero
        draw_map(13, 13, updated_map)
        #Todo add map boundraies
       #Todo move hero token
       #Todo add enemies
       #Todo move enemies
       #Todo add start position and goals
       #Todo add enemy ai
       #Todo add battles
       #Todo add items

        user_input = input('What would you like to do?: ')# prompts user input

        if is_quit(user_input):
            print('Quitting Gracefully')
            break
        elif user_input.lower().strip() == 'n':
            move_hero(0, -1, hero_location)
        elif user_input.lower().strip() == 's':
            move_hero(0, 1, hero_location)
        elif user_input.lower().strip() == 'e':
            move_hero(1, 0, hero_location)
        elif user_input.lower().strip() == 'w':
            move_hero(-1, 0, hero_location)
