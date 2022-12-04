import pathlib

from solution1 import main as sol1
from solution2 import main as sol2

fp = pathlib.Path(__file__).resolve()
wd = fp.parents[0]
test_file = wd.joinpath("test.txt")

def test_day4_sol1(capsys):
    # with capsys.disabled():
    solution = sol1(test_file)
    assert solution == 2


def test_day4_sol2(capsys):
    # with capsys.disabled():
    solution = sol2(test_file)
    assert solution == 4
