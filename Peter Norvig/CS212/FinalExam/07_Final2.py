"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools
import time

def dayafter(a, b): return a - b == 1
def elusive(option, x):
    a, b = option
    return (a is x and b is not x) or (a is not x and b is x)
def oneis(x, y):
    x1, x2 = x; y1, y2 = y
    return (x1 is y1 and x2 is y2) or (x1 is y2 and x2 is y1)

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    week =  Mon, Tue, Wed, Thu, Fri =  [1,2,3,4,5]
    orderingof5 = list(itertools.permutations(week))
    orderingof4 = list(itertools.permutations(week, 4))
    result = next([Hamming, Knuth, Minsky, Simon, Wilkes]
            for (Hamming, Knuth, Minsky, Simon, Wilkes) in orderingof5
            for (lap, droid, tablet, iphone) in orderingof4
            if Wed is lap
            if Fri is not tablet
            if elusive([iphone, tablet], Tue)
            for (programmer, writer, manager, designer) in orderingof4
            if tablet is not manager
            if writer is not Minsky
            if programmer is not Wilkes
            if designer is not droid
            if Thu is not designer
            #if Knuth is not manager
            if dayafter(Knuth, manager)
            if dayafter(Knuth, Simon)
            if oneis([programmer, droid], [Wilkes, Hamming])
            if oneis([lap, Wilkes], [Mon, writer])
            )
    return project(result)

def project(ordering):
    names = ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
    results = [''] * 5
    for i, name in enumerate(names):
        results[ordering[i]-1] = name
    return results

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result
