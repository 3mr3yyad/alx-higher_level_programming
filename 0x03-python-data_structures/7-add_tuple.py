#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = tu_x[0] if len(tu_x) > 0 else 0
    x2 = tu_x[1] if len(tu_x) > 1 else 0
    y1 = tu_y[0] if len(tu_y) > 0 else 0
    y2 = tu_y[1] if len(tu_y) > 1 else 0
    return (x1 + y1, x2 + y2)
