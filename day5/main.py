import re


with open("day5/input.txt") as f:
    lines = f.readlines()

num_crates = []
from_col = []
to_col = []

for line in lines:

    if re.match("move (\d*) from (\d) to (\d)", line):
        a, b, c = re.match("move (\d*) from (\d) to (\d)", line).groups()

        print(a,b,c)