from typing import List, Tuple
import numpy
from numpy import array
import matplotlib.pyplot as plt
import random
import traceback

directions = {
    'north': (1, 0),
    'south': (-1, 0),
    'east': (0, 1),
    'west': (0, -1)
}


def get_image(path: str, np_array: array) -> None:
    print(f"[*] Creating image: {path}")
    plt.rcParams["figure.figsize"] = (100, 100)
    plt.imshow(np_array, cmap='hot')
    plt.savefig(path)
    plt.close()


def get_direction(directions_list: List[str], probability: List[float]) -> Tuple:
    random_direction = random.choices(directions_list, probability)
    return directions[random_direction.pop()]


def get_random_positions(steps: int):

    current_position = [0, 0]
    directions_list = list(directions.keys())

    yield current_position

    for step in range(0, int(steps)):
        width, height = get_direction(directions_list, [0.25, 0.25, 0.25, 0.25])
        current_position[0] += width
        current_position[1] += height

        yield current_position


def get_map():
    all_w, all_h = get_random_positions(100000)

    row_dimensions = (min(all_w), max(all_w))
    height_dimensions = (min(all_h), max(all_h))

    row = {a: count for count, a in enumerate(list(range(row_dimensions[0], row_dimensions[1] + 1)))}
    height = {a: count for count, a in enumerate(list(range(height_dimensions[0], height_dimensions[1] + 1)))}

    geo_map = []
    for dimension, index in height.items():
        geo_map.append([0 for a in list(range(0, len(row)))])

    for count, w in enumerate(all_w):
        w_x = row[all_w[count]]
        h_x = height[all_h[count]]
        try:
            geo_map[h_x][w_x] += 1
        except KeyError:
            traceback.print_exc(limit=1)

    return array(geo_map)


def main():
    for i in range(0, 100):
        get_image(f'images/{i}.png')

    plt.show()


if __name__ == '__main__':
    main()

