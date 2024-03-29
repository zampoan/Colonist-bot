import math

def q1(x1,y1,x2,y2):
    facing = None
    a = abs(y1 - y2)
    b = abs(x1 - x2)
    c = (a**2 + b**2) ** (0.5)
    
    angle = math.asin(b/c)
    # radians =print(math.radians(angle))
    if angle > 0 and angle < 90:
        facing = 'NE'

    print(facing, angle)


def q2(arr):
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    
    [print(key) for key, value in counts.items() if value > 1]
    

def q3():
    """
    Calculate probability of second place car overtaking first
    ???
    """
    pass

# q1(2,3,7,7)
# q2([1,2,3,4,3,4,5])
