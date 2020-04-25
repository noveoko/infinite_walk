import random
import numpy
from matplotlib import pyplot
from typing import List, Tuple


directions = {
    'north': (1, 0),
    'south': (-1, 0),
    'east': (0, 1),
    'west': (0, -1)
}
directions_list = list(directions.keys())
directions_probability = [0.25, 0.25, 0.25, 0.25]
number_of_steps = 100000


def get_image(path: str, geo_map: numpy.array) -> None:
    print(f"[*] Creating image: {path}")
    pyplot.rcParams["figure.figsize"] = (100, 100)
    pyplot.imshow(geo_map, cmap='hot')
    pyplot.savefig(path)
    pyplot.close()


def get_direction(probability: List[float]) -> Tuple[int, int]:
    random_direction = random.choices(directions_list, probability)
    return directions[random_direction.pop()]


def get_random_positions(steps: int) -> Tuple[int, int]:

    cur_position = (0, 0)

    yield cur_position
    while steps:
        width, height = get_direction(directions_probability)
        new_position = (cur_position[0] + width, cur_position[1] + height)

        yield new_position

        cur_position = new_position
        steps -= 1


def set_dimension(new_dimension: int, old_dimension: Tuple[int, int]) -> Tuple[int, int]:
    return min(new_dimension, old_dimension[0]), max(new_dimension, old_dimension[1])


def get_map(positions: Tuple[int, int]) -> numpy.array:
    row_dimensions = [0, 0]
    height_dimensions = [0, 0]

    generated_positions = []
    for width_path, height_path in positions:
        row_dimensions = set_dimension(width_path, row_dimensions)
        height_dimensions = set_dimension(height_path, height_dimensions)
        generated_positions.append((width_path, height_path))

    row = {position: index
           for index, position in enumerate(range(row_dimensions[0], row_dimensions[1] + 1))
    }

    height = {position: index
              for index, position in enumerate(range(height_dimensions[0], height_dimensions[1] + 1))
    }

    geo_map = [[0 for _ in row] for _ in height]

    for step in generated_positions:
        w_x = row[step[0]]
        h_x = height[step[1]]
        geo_map[h_x][w_x] += 1

    return numpy.array(geo_map)


def main():
    path = 'image.png'
    get_image(path, get_map(get_random_positions(number_of_steps)))

    # pyplot.show()


if __name__ == '__main__':
    main()

