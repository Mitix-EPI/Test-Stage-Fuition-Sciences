#!/usr/bin/env python3

def update_direction(dir, action):
    if (action == "D"):
        dir += 1
        if (dir > 4):
            dir = 1
    if (action == "G"):
        dir -= 1
        if (dir < 1):
            dir = 4
    return dir


def set_direction(dir):
    if (dir == "N"):
        dir = 1
    elif (dir == "E"):
        dir = 2
    elif (dir == "S"):
        dir = 3
    else:
        dir = 4
    return dir

def get_direction(dir):
    if (dir == 1):
        dir = "N"
    elif (dir == 2):
        dir = "E"
    elif (dir == 3):
        dir = "S"
    else:
        dir = "W"
    return dir