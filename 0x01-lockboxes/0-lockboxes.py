#!/usr/bin/python3
"""
A Method to determine if all boxes can be opened.
Method returns True if all boxes can be opened or else
method returns False.
"""


def canUnlockAll(boxes):
    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True
