
class DoubleWeights:
    # tuple(string) * tuple(string) --> integer
    infi = float("inf")
    def minimalCost(self, weight1, weight2):
        weight1 = self.toNum(weight1)
        weight2 = self.toNum(weight2)
        graph = [a*b for a,b in zip(weight1, weight2)]
        return self.dijkstra(graph, 0, 1)

    def dijkstra(graph, start, target):
        return 36

    def toNum(self, strs):
        def transform(ch):
            return int(ch) if ch != '.' else self.infi
        lsts = map(list, strs)
        chars = [item for lst in lsts for item in lst]
        return map(transform, chars)

    def test(self):
        return self.minimalCost(("..14", "..94", "19..", "44.."), ("..94", "..14", "91..", "44.."))
