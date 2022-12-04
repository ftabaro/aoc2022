import pathlib

from .daysolution1 import main as sol1
from solution2 import main as sol2

fp = pathlib.Path(__file__).resolve()
wd = fp.parents[0]
test_file = wd.joinpath("test.txt")

def test_day2_sol1(capsys):
    # with capsys.disabled():
    solution = sol1(test_file)
    assert solution == 15


def test_day2_sol2(capsys):
    # with capsys.disabled():
    solution = sol2(test_file)
    assert solution == 12
import pathlib

from solution1 import main as sol1
from solution2 import main as sol2

fp = pathlib.Path(__file__).resolve()
wd = fp.parents[0]
test_file = wd.joinpath("test.txt")

def test_day3_sol1(capsys):
    # with capsys.disabled():
    solution = sol1(test_file)
    assert solution == 157


def test_day3_sol1(capsys):
    # with capsys.disabled():
    solution = sol2(test_file)
    assert solution == 70
import pathlib

from solution1 import main as sol1
from solution2 import main as sol2

fp = pathlib.Path(__file__).resolve()
wd = fp.parents[0]
test_file = wd.joinpath("test.txt")

def test_day1_sol1(capsys):
    # with capsys.disabled():
    solution = sol1(test_file)
    assert solution == 24000


def test_day1_sol1(capsys):
    # with capsys.disabled():
    solution = sol2(test_file)
    assert solution == 45000
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
