from Point import *

def make_segment(start, end):
    return (start, end)

def start_segment(segment):
    return segment[0]

def end_segment(segment):
    return segment[1]

def midpoint_segment(segment):
    x1 = x_point(start_segment(segment))
    y1 = y_point(start_segment(segment))
    x2 = x_point(end_segment(segment))
    y2 = y_point(end_segment(segment))
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return make_point(x, y)
