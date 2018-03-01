#!/usr/bin/env python3
from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])
Ride = namedtuple('Ride', ['start', 'finish', 'earliest', 'latest', 'distance'])

field_size = Pos(None, None)
vehicles = None  # TODO: this  should represent the vehicle's position, etc.
time_left = None
ride_bonus = None


def parse_input_file(input_file):
    global field_size, vehicles, time_left, ride_bonus

    rides = []
    with open(input_file) as f:
        setup = f.readline().split(" ")
        field_size = Pos(int(setup[0]), int(setup[1]))
        vehicles = [None] * int(setup[3])
        ride_bonus = int(setup[4])
        time_left = int(setup[5])

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


print ("size=",field_size)
print ("cars=",vehicles)
print ("time=",time_left)
print ("ride=",ride_bonus)
