# Created on Feb  2019
#
# @author: Mike Yuan
#
# This script tests the get_distnace function of the pydistrrr package.
#

import pytest
import pandas as pd
import numpy as np
from scipy.spatial import distance
from pydistrrr.get_distance import get_distance

# dummy input
point1 = [1, 1]
point2 = [1, 2]
point3 = [1, 2, 3, 4, 5]
point4 = [5, 4, 3, 2, 1]

empty_point = []
bad_point = ["2", "hello"]

# helper function


def get_manhhantan_dist(point1, point2):
    """
    Helper function to verfiy manhhantan distance
    """
    a1 = np.asarray(point1)
    a2 = np.asarray(point2)
    return np.sum(abs(a1 - a2))

# test cases


def test_correct_eclidean():
    """
    Test if the correct distance is return based on the metric
    """

    assert get_distance(
        point1, point2, metric="eclidean") == distance.euclidean(point1, point2)


def test_correct_cosine():
    """
    Test if the correct distance is return based on the metric
    """

    assert get_distance(
        point1, point2, metric="eclidean") == distance.cosine(point1, point2)


def test_correct_manhhantan():
    """
    Test if the correct distance is return based on the metric
    """

    assert get_distance(
        point1, point2, metric="eclidean") == get_manhhantan_dist(point1, point2)


def test_null_list_input():
    """
    Test if the Value error will be raised if one of the parameter is empty list
    """
    with pytest.raises(ValueError, match=r'.* empty list .*'):
        get_distance(point1, empty_point)
        get_distance(empty_point, point1)


def test_unequal_length_in_list():
    """
    Test if assertion error will be thrown if the lists have different length
    """
    with pytest.raises(AssertionError, match=r'.* empty list .*'):
        get_distance(point1, point3)
        get_distance(point3, point1)
