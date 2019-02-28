#!/usr/bin/env python3
from collections import namedtuple
import itertools
import functools
import random
import sys

Photo = namedtuple('Photo', ['id', 'tags'])


def parse_input_file(input_file):
    global field_size, vehicles, max_time, ride_bonus

    verticals, horizontals = [], []
    with open(input_file, 'r') as fh:
        num_photos = int(fh.readline())
        for id in range(0, num_photos):
            line = fh.readline()
            tags = line.rstrip('\n').split(' ')
            hv = tags.pop(0)
            tags.pop(0)
            photo = Photo(str(id), set(tags))
            if hv == 'V':
                verticals.append(photo)
            else:
                horizontals.append(photo)
    return verticals, horizontals


def pair_score(left, right):
    common = len(left.tags.intersection(right.tags))
    leftdiff = len(left.tags - right.tags)
    rightdiff = len(right.tags - left.tags)
    return min(common, leftdiff, rightdiff)


def permute_verticals(verticals):
    """Create a random list slides with vertical pairs"""
    result = []
    permutations = itertools.combinations(verticals, 2)
    for left, right in permutations:
        slide = Photo('{} {}'.format(left.id, right.id), left.tags.union(right.tags))
        result.append(slide)
    return result


def slides_score(slides):
    score = 0
    left = slides[0]
    for right in slides[1:]:
        score += pair_score(left, right)
        left = right
    return score


def render_permutation(permutation, filename):
    with open(filename, 'w') as fh:
        fh.write('{}\n'.format(len(permutation)))
        for slide in permutation:
            fh.write(slide.id + '\n')


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print ("usage: ./main.py IN_FILE OUT_FILE")
        sys.exit(1)
    verticals, slides = parse_input_file(sys.argv[1])
    slides.extend(permute_verticals(verticals))
    slides_permutation = itertools.permutations(slides, len(slides))
    best_score, best_permutation = 0, []
    for counter, permutation in enumerate(slides_permutation):
        score = slides_score(permutation)
        if score > best_score:
            print('Permutation: ', counter, score)
            best_permutation = permutation
            best_score = score
            render_permutation(best_permutation, sys.argv[2] + '-intermediate.txt')
    render_permutation(best_permutation, sys.argv[2])