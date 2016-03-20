# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    # Your code here
    def expand(d, u):
        if d < 0 or u > N-1 or text[d] != text[u]:
            return (d+1, u-1)
        return expand(d-1, u+1)
    
    def lenx(pair): return pair[1] - pair[0]
    
    N = len(text)
    if N == 0 : return (0, 0)
    text = text.lower()

    allpairs = [expand(i, i) for i in range(N)]
    allpairs.extend([expand(i, i+1) for i in range(N-1) if text[i] == text[i+1]])

    (d, u) = max(allpairs, key=lenx)
    return (d, u+1)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()

#### The solution of Peter Norvig is somewhat similar 
#====================================================
def longest_subpalindrome_slice(text):
    def grow(start, end):
        while (start > 0 and end < N 
                and text[start-1] == text[end]):
            start -= 1; end += 1
        return (start, end)
    def lenx(pair) : a, b = pair; return b-a

    N = len(text)
    text = text.lower()
    if text == '': return (0,0)

    candidates = [grow(start, end) 
            for start in range(N) 
            for end in (start, start+1)]
    return max(candidates, key=lenx)

#### An old solution of mine, which also work but is ugly #####
#===============================================================
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = text.upper()
    if text == '': return (0, 0)
    records = []
    positions = range(2*len(text) )
    for i in positions:
        records.append( calculate(i, text) )
    #print(records)
    
    value = max(records)
    pos = records.index(value)
    #if locate%2 != 0 :
    #    rlocate = int((locate - 1)/2)
    #    print(rlocate - (value-1)/2,  rlocate + (value-1)/2)
    #    return (rlocate - (value-1)/2,  rlocate + (value-1)/2)
    #else :
    #    rlocate = locate/2
    #    print(rlocate - value/2, rlocate + value/2 - 1)
    #    return (rlocate - value/2, rlocate + value/2 - 1)
    if pos % 2 == 0:
        return ( (int)(pos/2 - value/2), (int)(pos/2 + value/2))
    return ((int)((pos - 1)/2 -(value-1)/2), (int)((pos-1)/2 + (value-1)/2 + 1))

def calculate(i, s):
    pos = int(i/2)
    if i % 2 == 0 :
        return extendPalin(pos - 1, pos, s)
    return extendPalin(pos - 1, pos + 1, s) 

def extendPalin(start, end, s):
    if start < 0 or  end >= len(s) or s[start] != s[end] :
        return end - start - 1
    return extendPalin(start-1, end + 1, s)
#===============================================================

