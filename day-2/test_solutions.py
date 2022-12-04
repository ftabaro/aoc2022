from solution1 import main as sol1
from solution2 import main as sol2


def test_sol1(capsys):
    # with capsys.disabled():
    solution = sol1("test.txt")
    assert solution == 15


def test_sol2(capsys):
    # with capsys.disabled():
    solution = sol2("test.txt")
    assert solution == 12
