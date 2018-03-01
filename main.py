#!/usr/bin/env python3

def parse_input_file(input_file):
    rides = []
    with open(input_file) as f:
        f.readline()
        for line in f:
            e = line.split(" ")
            rides.append ( ((e[0],e[1]), (e[2], e[3]), (e[4], str.replace(e[5], "\n", ""))) )

    return rides

from pprint import pprint
pprint (parse_input_file("Dataset/a_example.in"))
