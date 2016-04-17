class ABBADiv1:
    def canObtain(self, initial, target):
        dict_b2s = {True:"Possible", False:"Impossible"}
        return dict_b2s[self.canObtainRec(initial, target)]

    def canObtainRec(self, initial, target):
        def reverse(string): return string[::-1]
        def head(string): return string[0:-1]
        if len(initial) == len(target):
            return initial == target
        if target[-1] == 'B': result = self.canObtainRec(initial, head(reverse(target)))
        else: result = self.canObtainRec(initial,head(target)) \
                or self.canObtainRec(initial, head(reverse(target)))
        return result

    def test(self):
        assert self.canObtain("BAAAAABAA", "BAABAAAAAB") == "Possible"
        assert self.canObtain('A', 'ABBA') == "Impossible"
        assert self.canObtain("AAABBAABB", "BAABAAABAABAABBBAAAAAABBAABBBBBBBABB") == "Possible"
        assert self.canObtain("AAABAAABB", "BAABAAABAABAABBBAAAAAABBAABBBBBBBABB") == "Impossible"
        return True
