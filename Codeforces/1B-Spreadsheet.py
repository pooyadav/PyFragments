# Performance on Codeforces: 2370ms, 6200KB.
# Could be improved.

import re

def main():
    n = int(raw_input())
    for i in range(n):
        s = raw_input()
        print transform(s)

def transform(s):
    flag, token = analyze(s) 
    if  flag== 1 : return token2rc(token)
    return token2ex(token)

# codenum: 1 for Excel style, 2 for RXCY style.
# token: (int, int) --> (row, col); row and col <= 10^6
def analyze(s):
    m = re.match('R[0-9]+C[0-9]+', s)
    if  m == None:
        codes = 1
        m1 = re.match('[A-Z]+', s)
        col = excel2int(s[0:m1.end()])
        row = int(s[m1.end():])
    else:
        codes = 2
        [_, row, col] = re.split('[A-Z]', s)
        row = int(row); col = int(col);
    return (codes, (row, col))

def token2ex(t):
    r, c = t
    return exceldec(c) + str(r)

def token2rc(t):
    r, c = t
    return 'R' + str(r) + 'C' + str(c)

#int to a excel-style number system
def exceldec(num):
    def tolove(x): 
        assert x >= 1 and x <=26
        return str(unichr(x+64))
    acc = ''
    while True:
        mod = (num - 1) % 26 + 1
        num = (num - mod) / 26
        acc = tolove(mod) + acc
        if num == 0: break
    return acc 

# string, say, 'AB' to number 28
def excel2int(string):
    def toloveru(ch): return ord(ch) - 64
    nums = map(toloveru, list(string))
    acc = 0
    for i in nums:
        acc = acc * 26 + i
    return acc

def test():
    string = 'R23C55';
    assert excel2int('BC') == 55
    assert excel2int('AA') == 27
    assert exceldec(55) == 'BC'
    assert exceldec(25) == 'Y'
    assert exceldec(52) == 'AZ'
    assert exceldec(28) == 'AB'
    assert exceldec(27) == 'AA'
    assert analyze(string) == (2, (23, 55))
    assert analyze('BC23') == (1, (23, 55))
    assert token2rc((23, 55)) == 'R23C55'
    assert token2ex((23, 55)) == 'BC23'
    print 'test pass'


main()
