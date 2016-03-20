import random
from collections import defaultdict

def shuffle1(deck):
    # O(N**2)
    # incorrect distribution
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        deck[i], deck[j] = deck[j], deck[i]
def shuffle2(deck):
    # O(N**2)
    # incorrect distribution?    
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2a(deck):
    # http://forums.udacity.com/cs212-april2012/questions/3462/better-implementation-of-shuffle2
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        j = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle3(deck):
    # O(N)
    # incorrect distribution    
    N = len(deck)
    for i in range(N):
        j = random.randrange(N)
        deck[i], deck[j] = deck[j], deck[i]
 
def shuffle(deck):
    # Knuth method
    n = len(deck)
    for i in range(n-1):
        j = random.randrange(i, n)
        deck[i], deck[j] = deck[j], deck[i]

def test_shuffle(shuffler, deck="abc", n=10000):
    d = defaultdict(int)
    for _ in range(n):
        dec = list(deck)
        shuffler(dec)
        d[''.join(dec)] += 1
    #print d.items()
    showdict(shuffler, deck, d, n)
 
def showdict(f, deck, d, n):
    print "%s(%s):" % (f.__name__, deck)
    for key, item in d.items():
        print "%s: %.2f%%" % (key, 100. *item / n)
    print 

def test():
    shufflers = [shuffle, shuffle1, shuffle2, shuffle2a, shuffle3]
    decks = ["abc"]
    for f in shufflers:
        for d in decks:
            test_shuffle(f, d)
