#SRM 441 DIV 1
#Takes too much space

from itertools import permutations

class PerfectPermutation:
    def reorder(self, P):
        # P: tuple(int), return:int

        def similarity(perm):
            diff = [i!=j for i,j in zip(perm, P)]
            diff = map(int, diff)
            return sum(diff)

        permlist = permutations(list(P))
        permlist = list(permlist) # List of tuples;
        #print permlist

        perfects = filter(self.isPerfect, permlist)
        print perfects

        lengths = map(similarity, perfects)
        print lengths
        return min(lengths)

    def isPerfect(self, perm):
        n = len(perm)
        child = [0]*n
        for i in range(1, n):
            child[i] = perm[child[i-1]]
        if sorted(child) == list(range(n)):
            return True
        return False

def test():
    x = PerfectPermutation()
    x.reorder((2,0,1))
    x.reorder((0, 5, 3, 2, 1, 4))
    #x.reorder(())
        

