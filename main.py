#!/usr/bin/env python3
from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])
Ride = namedtuple('Ride', ['start', 'finish', 'earliest', 'latest', 'distance'])

def parse_input_file(input_file):
    rides = []
    with open(input_file) as f:
        f.readline()
        for line in f:
            e = line.split(" ")
            start = Pos(int(e[0]), int(e[1]))
            finish = Pos(int(e[2]), int(e[3]))
            ride = Ride(start, finish, int(e[4]), int(str.replace(e[5], "\n", "")), compute_distance(start, finish))
            rides.append(ride)

    return rides

def compute_distance(start, finish):
    return abs(start.x - finish.x) + abs(start.y - finish.y)


from pprint import pprint
rides = parse_input_file("Dataset/a_example.in")
pprint(rides)