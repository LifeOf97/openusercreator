
def test_1():
    name = "Python"
    title = "Python is my goto programming language."
    assert name in title


def test_2():
    assert 12 < 10


def test_3():
    one = 'a'
    two = 'a'
    assert len(one) == len(two)