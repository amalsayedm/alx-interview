#!/usr/bin/python3


def canUnlockAll(boxes):
    if isinstance(boxes, list) and boxes:
        boolboxes= [False] * len(boxes)
        for i, box in enumerate(boxes):
            for element in box:
                if element > len(boxes):
                    boolboxes[element] = True
        return boolboxes
        
