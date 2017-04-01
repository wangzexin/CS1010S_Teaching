def make_point(x, y):
    return str(x) + " " + str(y)

def x_point(pt):
    x = pt.index(" ")
    return float(pt[:x])

def y_point(pt):
    x = pt.index(" ")
    return float(pt[x+1:])

def print_point(p):
    print ("(", x_point (p), ",", y_point (p), ")")
