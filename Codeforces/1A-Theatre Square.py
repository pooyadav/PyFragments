#a = raw_input().split(' ')
import sys
#n = int(raw_input())
#m = int(raw_input())
#a = int(raw_input())
s = raw_input()
tokens = s.split(' ')
[n, m, a] = map(int, tokens)

def judge(n, m, a):
    re = 0
    x = n/a
    y = m/a
    if n <= a:
        if m <= a : return 1
        elif m%a ==0 : return y
        else: return y+1
    else:
        if n%a == 0:
            if m <= a: return x
            elif m%a == 0: return x*y
            else: return x*(y+1)
        else:
            if m <= a: return x+1
            elif m%a == 0: return (x+1)*y
            else: return (x+1)*(y+1)
    return 0

re = judge(n,m,a)
print re
#write = sys.stdout.write
#write(tostring(re))