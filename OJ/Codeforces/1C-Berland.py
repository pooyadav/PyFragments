import sys
import math

"""
digree < 100, which leave only two possiblilities:
equilateral triangle, and rectangle
"""
def main():
    ps = []
    for line in sys.stdin:
        (a, b) = line.split(' ')
        ps.append((float(a), float(b)))
    if is_equilateral_tri(ps[0], ps[1], ps[2]):
        l = distance(ps[0], ps[1])
        s = math.sqrt(3) * l * l / 4
    else: #suppose honest input  
        a = distance(ps[0], ps[1])
        b = distance(ps[2], ps[1])
        c = distance(ps[0], ps[2])
        if a > b and a > c : s = b * c
        elif b > a and b > c: s = a * c
        else: s = a * b
    print("%.6f" % s)

def is_equilateral_tri(p1, p2, p3):
    d1 = distance(p1, p2)
    d2 = distance(p2, p3)
    d3 = distance(p1, p3)
    return math.isclose(d1, d2, rel_tol=1e-06) and \
        math.isclose(d2, d3, rel_tol=1e-06)

def distance(p1, p2):
    return math.sqrt(pow((p2[0] - p1[0]), 2) +  
        pow((p2[1] - p1[1]), 2))

def test():
    p1 = (0.0, 0.0)
    p2 = (0.5, 0.5 * math.sqrt(3))
    p3 = (1.0, 0.0)
    p4 = (1.0, 1.0)
    
    assert is_equilateral_tri(p1, p2, p3) == True
    assert is_equilateral_tri(p1, p2, p4) == False
    p5 = (71.756151, 7.532275)
    p6 = (-48.634784, 100.159986)
    p7 = (91.778633, 158.107739)
    print(distance(p5, p6))
    print(distance(p6, p7))
    print(distance(p5, p7))
    assert is_equilateral_tri(p5, p6, p7) == True
    
#test()
main()
