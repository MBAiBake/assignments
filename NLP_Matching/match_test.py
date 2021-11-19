from match_lib import match


def test_match1():
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"


def test_match2():
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"


def test_match3():
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"


def test_match4():
    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"


def test_match5():
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"


def test_match6():
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"


def test_match7():
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"


def test_match8():
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"


def test_match9():
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"


def test_match10():
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"


def test_match11():
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"


def test_match12():
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"


def test_match13():
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"


def test_match14():
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"


def test_match15():
    # this last case is a strange one, but it exposes an issue with the way we've
    # written our match function
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"