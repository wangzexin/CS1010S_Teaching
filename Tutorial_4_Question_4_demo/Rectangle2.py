from Vector import *

def make_rectangle(height, width):
    # Check if this can make a rectangle or not
    # Check if connected
    if x_point(height) != x_point(width) and x_point(height) != y_point(width) and y_point(height) != x_point(width) and y_point(height) != y_point(width):
        return "The two segments are not properly connected."
    # Check if perpendicular
    vector_height = get_vector(height)
    vector_width = get_vector(width)
    if not(perpendicular_vector(vector_height, vector_width)):
        return "The two segments are not perpendicular."
    return (width, height)

def height_rect(rect):
    return rect[1]

def width_rect(rect):
    return rect[0]

def area_rectangle(rect):
    height = height_rect(rect)
    width = width_rect(rect)
    vector_height = get_vector(height)
    vector_width = get_vector(width)
    length_height = get_length_vector(vector_height)
    length_width = get_length_vector(vector_width)
    return length_height * length_width

def perimeter_rectangle(rect):
    height = height_rect(rect)
    width = width_rect(rect)
    vector_height = get_vector(height)
    vector_width = get_vector(width)
    length_height = get_length_vector(vector_height)
    length_width = get_length_vector(vector_width)
    return (length_height + length_width) * 2
