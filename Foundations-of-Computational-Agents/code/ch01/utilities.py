import random


def argmax(gen):
    """gen is a generator of (element,value) pairs, where value is a real.
    argmax returns an element with maximal value.
    If there are multiple elements with the max value, one is returned at random.
    """
    maxv = float('-Infinity')
    maxvals = []
    for (e, v) in gen:
        if v > maxv:
            maxvals, maxv = [e], v
        elif v == maxv:
            maxvals.append(e)
    return random.choice(maxvals)


def filip(prob):
    """return ture with probalility prob"""
    return random.random() < prob


def dict_union(d1, d2):
    """returns a dictionary that contains the keys of d1 and d2.
    The value for each key that is in d2 is the value from d2,
    otherwise it is the value from d1.
    This does not have side effects.
    """
    d = dict(d1)  # copy d1
    d.update(d2)
    return d


def test():
    """test part of utilites"""
    assert argmax(enumerate([1, 6, 55, 3, 55, 23])) in [2, 4]
    assert dict_union({
        1: 4,
        2: 5,
        3: 4
    }, {
        5: 7,
        2: 9
    }) == {
        1: 4,
        2: 9,
        3: 4,
        5: 7
    }
    print("Passed unit test in utilities")


if __name__ == '__main__':
    test()
