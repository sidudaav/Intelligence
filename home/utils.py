def get_value(inp):
    length = len(inp)
    if "xy" in inp:
        return int((inp[:length - 2]))
    else:
        return int((inp[:length - 1]))

def get_direction(inp):
    if "xy" in inp:
        return "xy"
    elif "x" in inp:
        return "x"
    else:
        return "y"

def map_point():
    pass