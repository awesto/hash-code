#!/usr/bin/env python3
from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])
Ride = namedtuple('Ride', ['id', 'start', 'finish', 'earliest', 'latest', 'distance'])

field_size = Pos(None, None)
vehicles = []
max_time = None
ride_bonus = None

class Car(object):
    def __init__(self, id):
        self.id = id
        self.current = Pos(0, 0)
        self.occupied_until = 0
        self.rides = []

    def drive(self, ride, current_time):
        dist_car_start = compute_distance(self.current, ride.start)
        dist_start_dest = compute_distance(ride.start, ride.finish)
        self.occupied_until = current_time + dist_car_start + dist_start_dest
        self.current = ride.finish
        self.rides.append(ride)

def parse_input_file(input_file):
    global field_size, vehicles, max_time, ride_bonus

    ride_index = 0
    rides = []
    with open(input_file) as f:
        setup = f.readline().split(" ")
        field_size = Pos(int(setup[0]), int(setup[1]))
        vehicles = [Car(i) for i in range(int(setup[3]))]
        ride_bonus = int(setup[4])
        max_time = int(setup[5])

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

    if current_time + dist_car_start < ride.earliest:
        # don't pick up the rider too early
        return 0

    dist_start_dest = compute_distance (ride.start, ride.finish)

    full_distance = dist_car_start + dist_start_dest
    if full_distance > ride.latest - current_time:
        # this ride can not be fulfilled in time => no reward
        return 0

    reward = dist_start_dest

    if current_time + dist_car_start == ride.earliest:
        # bonus if we pick up at exact time
        reward += 2

    return reward

def greedy_select_ride(car: Car, current_time: int) -> Ride:
    print('=== {} ==='.format(current_time))
    combinations = []
    for ride in rides:
        reward = compute_reward(car, ride, current_time)
        if reward == 0:
            continue
        combinations.append((ride, car, reward))
    combinations = sorted(combinations, key=lambda t: t[2], reverse=True)
    return combinations[0][0]


if __name__ == '__main__':

    rides = parse_input_file("Dataset/a_example.in")

    for current_time in range(max_time):
        for car in vehicles:
            if car.occupied_until > current_time:
                continue
            try:
                ride = greedy_select_ride(car, current_time)
            except IndexError:
                continue
            car.drive(ride, current_time)
            rides.remove(ride)
        if not rides:
            break


    for car in vehicles:
        print (len(car.rides), *[ride.id for ride in car.rides])
