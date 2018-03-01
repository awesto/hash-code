#!/usr/bin/env python3
from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])
Ride = namedtuple('Ride', ['id', 'start', 'finish', 'earliest', 'latest', 'distance'])

class Car(object):
    def __init__(self):
        current = Pos(0, 0)
        destination = None
        occupied = False



field_size = Pos(None, None)
vehicles = []
time_left = None
ride_bonus = None


def parse_input_file(input_file):
    global field_size, vehicles, time_left, ride_bonus

    ride_index = 0
    rides = []
    with open(input_file) as f:
        setup = f.readline().split(" ")
        field_size = Pos(int(setup[0]), int(setup[1]))
        vehicles = [Car()] * int(setup[3])
        ride_bonus = int(setup[4])
        time_left = int(setup[5])

        for line in f:
            e = line.split(" ")
            start = Pos(int(e[0]), int(e[1]))
            finish = Pos(int(e[2]), int(e[3]))
            ride = Ride(ride_index, start, finish, int(e[4]), int(str.replace(e[5], "\n", "")), compute_distance(start, finish))
            rides.append(ride)
            ride_index += 1

    return rides

def compute_distance(start, finish):
    return abs(start.x - finish.x) + abs(start.y - finish.y)


def compute_reward (car, ride, current_time):
    # calculate what reward we'd get if we'd start driving there now

    dist_car_start = compute_distance (car.current, ride.start)
    dist_start_dest = compute_distance (ride.start, ride.finish)

    full_distance = dist_car_start + dist_start_dest
    if full_distance > (current_time-ride.latest):
        return 0

    reward = dist_start_dest

    if current_time + dist_car_start == ride.earliest:
        reward += 2

    return reward

from pprint import pprint
rides = parse_input_file("Dataset/a_example.in")
pprint(rides)

