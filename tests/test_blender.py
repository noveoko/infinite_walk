# TODO import os
import pytest
from ..blender import *


@pytest.fixture
def path():
    return 'image'


@pytest.fixture
def geo_map():
    return numpy.array([[0, 0]])  # FIXME


def test_get_image(path, geo_map):
    pass
    # TODO get_image(path, geo_map)
    # TODO assert os.path.exists(path)


def test_get_direction(probability):
    assert isinstance(probability, list)
    assert isinstance(probability.pop(), float)

    assert isinstance(get_direction(probability), tuple)
