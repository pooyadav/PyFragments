import itertools
import math

class MultiplicationTable2Easy:
    # Tuple(integer) * tuple(integer) --> string
    result = {True:"Good", False:"Not Good"}
    def isGoodSet(self, table, t):
        self.table = table
        self.n = int(math.sqrt(len(table)))
        
        pairs = self.toProduct(t)
        numbers = map(self.translate, pairs)
        r = all([n in t for n in numbers])
        return self.result[r]

    # tuple -> generator
    def toProduct(self, t):
        return itertools.product(t, repeat=2)

    # generator -> integer
    def translate(self, pair):
        i, j = pair
        return self.table[j + self.n * i]

    def test(self):
        print self.isGoodSet((1, 1, 2, 3, 1, 0, 2, 3, 3, 3, 0, 3, 2, 2, 2, 0), (1,0)) #g
        print self.isGoodSet((1, 1, 2, 3, 1, 0, 2, 3, 3, 3, 0, 3, 2, 2, 2, 0), (2,3)) # Ng
        print self.isGoodSet((1, 1, 2, 3, 1, 0, 2, 3, 3, 3, 0, 3, 2, 2, 2, 0), (0,1,2,3)) #g
        print self.isGoodSet((1, 1, 2, 3, 1, 0, 2, 3, 3, 3, 0, 3, 2, 2, 2, 0), (1,)) #ng
        print self.isGoodSet((2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2), (2,4,5)) #G
        print self.isGoodSet((2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2, 2,2,2,2,2,2), (0,1,3,4,5)) #NG


### Other People's Solution:

def isGoodSet2(self, talbe, t):
	n = int(math.sqrt(len(table)))
	for x in t:
		for y in t:
			if not table[x*n + y]: return 'Not Good'
    return 'Good'
