import itertools

#### Version 1
#class CliqueParty:
#    # tuple(int) * integer -> integer
#    def maxsize(self, a, k):
#        for i in range(len(a), 0, -1):
#            subsets = itertools.combinations(a, i)
#            if any([self.ksmooth(self.s2d(s), k) for s in subsets]): 
#                return i
#        return 0
#
#    # tuple(int) -> set(int)
#    def s2d(self, s):
#        pairs = itertools.combinations(s, 2)
#        return set(map(lambda (x,y): abs(x-y), pairs))
#
#    def ksmooth(self, d, k):
#        return max(d) <= min(d) * k

### Version 2
class CliqueParty:
    # tuple(int) * integer -> integer
    def maxsize(self, a, k):
        for i in range(len(a), 0, -1):
            subsets = itertools.combinations(a, i)
            subsets = self.uniq(subsets, lambda lst: (min(lst), max(lst)))
            if any([self.ksmooth(self.s2d(s), k) for s in subsets]): 
                return i
        return 0

    # tuple(int) -> set(int)
    def s2d(self, s):
        pairs = itertools.combinations(s, 2)
        return set(map(lambda (x,y): abs(x-y), pairs))

    def ksmooth(self, d, k):
        return max(d) <= min(d) * k

    def uniq(self, lst, func):
        output = []; explored = set()
        for x in lst: 
            foo = func(x)
            if foo not in explored: 
                explored.add(foo)
                output.append(x)
        return output

    def test(self):
        assert self.maxsize((1,2,3), 1) == 2
        assert self.maxsize((4,10,5,6), 2) == 3
        assert self.maxsize((10,9,25,24,23,30), 7) == 4
        assert self.maxsize((1,2,3,4,5,6), 3) == 4
        return True
