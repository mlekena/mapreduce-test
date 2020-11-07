import math
from functools import reduce


def test_func():
    return "HELLO WORLD"


def euc_dist(lhs, rhs):
    assert(len(lhs) == len(rhs)
           ), "euclidian distance candidates are not the same length. :("
    sum_under = reduce(lambda val1, val2: val1 + val2,
                       map(lambda lhs_rhs: (
                           lhs_rhs[0] - lhs_rhs[1])**2, zip(lhs, rhs))
                       )
    return math.sqrt(sum_under)


def to_numbers(candidates):
    try:
        the_converted = list(map(lambda s: float(s), candidates))
        return the_converted
    except ValueError:
        print("BAD INPUT: {}".format(candidates))
        exit("Failed to convert integers. Terminating exceptional path.")


def sum_arrays(lhs, rhs):
    return list(map(lambda pair: pair[0] + pair[1], zip(lhs, rhs)))


def centroid_to_string(centroid):
    return list(map(lambda idx: "{}".format(
                ",".join("%10.3f" % x for x in centroid[idx])), range(4)))
