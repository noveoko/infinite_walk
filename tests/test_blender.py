import os
import pytest
from numpy import array
from ..blender import *


@pytest.fixture
def path():
    return ''


def test_get_image(path, np_array):
    assert isinstance(path, str)
    assert path.endswith('.png')
    assert os.path.exists(path)

    assert isinstance(np_array, array)


def test_get_direction(directions_list, probability):
    assert isinstance(directions_list, list)
    assert isinstance(directions_list.pop(), str)
    assert isinstance(probability, list)
    assert isinstance(probability.pop(), float)

    assert isinstance(get_direction(directions_list, probability), tuple)
