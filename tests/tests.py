"""
AoC 2022 tests
"""

import pathlib
import sys

# Add tests parent directory to python path
root = pathlib.Path(sys.path[0]).parents[0]
sys.path.append(str(root))

# import all solutions
from day1.solution1 import main as d1s1
from day1.solution2 import main as d1s2

from day2.solution1 import main as d2s1
from day2.solution2 import main as d2s2

from day3.solution1 import main as d3s1
from day3.solution2 import main as d3s2

from day4.solution1 import main as d4s1
from day4.solution2 import main as d4s2


# Define paths to test data
fp = pathlib.Path(__file__).resolve()
testdata = fp.parents[0].joinpath("testdata")

test_files = {
    f"day{i}": str(testdata.joinpath(f"day{i}.txt")) for i in range(1, 25)
}

########
# DAY1 #
########


def test_day1_sol1():
    solution = d1s1(test_files["day1"])
    assert solution == 24000


def test_day1_sol2():
    solution = d1s2(test_files["day1"])
    assert solution == 45000


#########
# DAY 2 #
#########


def test_day2_sol1():
    solution = d2s1(test_files["day2"])
    assert solution == 15


def test_day2_sol2():
    solution = d2s2(test_files["day2"])
    assert solution == 12


#########
# DAY 3 #
#########


def test_day3_sol1():
    solution = d3s1(test_files["day3"])
    assert solution == 157


def test_day3_sol2():
    solution = d3s2(test_files["day3"])
    assert solution == 70


#########
# DAY 4 #
#########


def test_day4_sol1():
    solution = d4s1(test_files["day4"])
    assert solution == 2


def test_day4_sol2():
    solution = d4s2(test_files["day4"])
    assert solution == 4
