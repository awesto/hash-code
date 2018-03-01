#!/usr/bin/env python3
from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])
Ride = namedtuple('Ride', ['start', 'finish', 'earliest', 'latest'])

def parse_input_file(input_file):
    rides = []
    with open(input_file) as f:
        f.readline()
        for line in f:
            e = line.split(" ")
            start = Pos(e[0], e[1])
            finish = Pos(e[2], e[3])
            ride = Ride(start, finish, e[4], str.replace(e[5], "\n", ""))
            rides.append(ride)

    return rides

from pprint import pprint
pprint (parse_input_file("Dataset/a_example.in"))
