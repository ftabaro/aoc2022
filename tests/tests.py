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

from day5.solution1 import main as d5s1
from day5.solution2 import main as d5s2

from day6.solution1 import main as d6s1
from day6.solution2 import main as d6s2

from day7.solution1 import main as d7s1
from day7.solution2 import main as d7s2

from day8.solution1 import main as d8s1
from day8.solution2 import main as d8s2

from day9.solution1 import main as d9s1
from day9.solution2 import main as d9s2

from day10.solution1 import main as d10s1
from day10.solution2 import main as d10s2


# Define paths to test data
fp = pathlib.Path(__file__).resolve()
testdata = fp.parents[0].joinpath("testdata")
test_files = testdata.glob("*.txt")
test_files = [p.absolute() for p in test_files]
test_files = {p.name.replace(".txt", ""): str(p) for p in test_files}


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


#########
# DAY 5 #
#########


def test_day5_sol1():
    solution = d5s1(test_files["day5"])
    assert solution == "CMZ"


def test_day5_sol2():
    solution = d5s2(test_files["day5"])
    assert solution == "MCD"


#########
# DAY 6 #
#########


def test_day6_sol1():
    solution = d6s1(test_files["day6"])
    assert solution == [7, 5, 6, 10, 11]


def test_day6_sol2():
    solution = d6s2(test_files["day6"])
    assert solution == [19, 23, 23, 29, 26]


#########
# DAY 7 #
#########


def test_day7_sol1():
    solution = d7s1(test_files["day7"])
    assert solution == 95437


def test_day7_sol2():
    solution = d7s2(test_files["day7"])
    assert solution == 24933642


#########
# DAY 8 #
#########


def test_day8_sol1():
    solution = d8s1(test_files["day8"])
    assert solution == 21


def test_day8_sol2():
    solution = d8s2(test_files["day8"], 1, 2)
    assert solution == 4

    solution = d8s2(test_files["day8"], 3, 2)
    assert solution == 8

#########
# DAY 9 #
#########


def test_day9_sol1():
    solution = d9s1(test_files["day9"])
    assert solution == 13


def test_day9_sol2():
    solution = d9s2(test_files["day9"])
    assert solution == 1


def test_day9_sol2_v2():
    solution = d9s2(test_files["day9s2"])
    assert solution == 36

############
## DAY 10 ##
############


def test_day10_sol1():
    solution = d10s1(test_files["day10"])
    assert solution == 13140


def test_day10_sol2():
    sol = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    
    solution = d10s2(test_files["day10"])
    assert solution == sol
