from assets import TileToken, bcolors


def generate_tile_points(radius):
    tile_points = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if (x ** 2) + (y ** 2) <= radius ** 2:
                tile_points.append((x, y))
    return tile_points


def map_tile_points(radius):
    map_points = {}
    tile_points = generate_tile_points(radius)
    for i in tile_points:
        map_points[i] = TileToken("#", "91", "floor tile 5' x 5'")
    return map_points


def map_canvas_points(x_values, y_values, map_tiles):
    canvas_points = {}
    for x in range(-x_values, x_values + 1):
        for y in range(y_values, -y_values - 1, -1):
            if (x, y) in map_tiles:
                canvas_points[(x, y)] = map_tiles[(x, y)]
            else:
                canvas_points[(x, y)] = TileToken(".", "94", "water")
    return canvas_points



def load_map(canvas_x, canvas_y, radius):
    map_tiles = map_tile_points(radius)
    x_values = canvas_x // 2
    y_values = canvas_y // 2
    canvas = map_canvas_points(x_values, y_values, map_tiles)

    return canvas
