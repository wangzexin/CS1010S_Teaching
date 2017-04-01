from Segment import *

def get_vector(segment):
    x1 = x_point(start_segment(segment))
    y1 = y_point(start_segment(segment))
    x2 = x_point(end_segment(segment))
    y2 = y_point(end_segment(segment))
    return (x2 - x1, y2 - y1)

def get_length_vector(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5

def perpendicular_vector(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] == 0
