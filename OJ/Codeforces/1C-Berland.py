import sys
import math

N = 1000



def find_circle_center(p1, p2, p3):
    (x1, y1) = p1 
    (x2, y2) = p2 
    (x3, y3) = p3 
    # the perpendicular bisectors linear function is either 
    # A*x + B*y = B * y_mid + A * x_mid, or x = x_mid when y_1 == y_2
    # where A = x_2 - x_1 and B = y_2 - y_1
    # The rest part is just solving two linear systems
    # See: https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines-in-python
    
    def average(a, b): return (a + b) / 2
    # Line 1: the p1-p2 perpendicular
    x_mid1 = average(x1, x2); y_mid1 = average(y1, y2)
    if y1 == y2:
        L1 = (1, 0, -x_mid1)
    else:
        A1 = x2 - x1; B1 = y2 - y1;
        C1 = B1 * y_mid1 + A1 * x_mid1
        L1 = (A1, B1, -C1)
    print(L1)

    x_mid2 = average(x2, x3); y_mid2 = average(y2, y3)
    if y2 == y3:
        L2 = (1, 0, -x_mid2)
    else:
        A2 = x3 - x2; B2 = y3 - y2;
        C2 = B2 * y_mid2 + A2 * x_mid2
        L2 = (A2, B2, -C2)
    print(L2)

    xp = intersection(L1, L2) 
    if xp:
        print(xp)
        return xp 
    print("No single Intersection point detected.")
    return False

# def line(p1, p2):
#    A = (p1[1] - p2[1])
#    B = (p2[0] - p1[0])
#    C = (p1[0]*p2[1] - p2[0]*p1[1])
#    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return -x, -y
    else:
        return False

def distance(p1, p2):
    return math.sqrt(pow((p2[0] - p1[0]), 2) +  
        pow((p2[1] - p1[1]), 2))

def near_integer(num):
    u = math.ceil(num);
    l = math.floor(num);
    print("nearest:", num-l, num, u-num)
    return math.isclose(u, num, rel_tol=1e-03) \
        or math.isclose(l, num, rel_tol=1e-03)

def main():
    ps = []
    fin = open('input.txt', 'r')
    for line in fin.readlines():
    #for line in sys.stdin:
        (a, b) = line.split(' ')
        ps.append((float(a), float(b)))
    center = find_circle_center(ps[0], ps[1], ps[2])
    R = distance(center, ps[0])
    # find the smallest value of n that gives a near-integer value of s
    n = 0
    for n in range(3, N+1):
        print(n)
        s = 2 * R * math.sin(math.pi / n)
        if # s fit SOME condition
            break
        else:
            continue
    if n == 0:
        print("Error: input invalid.")
        return
    n= 5
    print("sides number is: %d" % n)
    area = 1 / 2 * n * R * R * math.sin(2 * math.pi / n)
    print("%.6f" % area)
    return area

def test():
    p1 = (0.0, 0.0)
    p2 = (0.5, 0.5 * math.sqrt(3))
    p3 = (1.0, 0.0)
    p4 = (1.0, 1.0)
    
    
    p5 = (71.756151, 7.532275)
    p6 = (-48.634784, 100.159986)
    p7 = (91.778633, 158.107739)
    

#test()
main()
