#### Topcoder: ABBA

### Version 1:

#class ABBA:
#    def canObtain(self, initial, target):
#        if len(initial) == len(target):
#            return initial == target
#        return self.canObtain(self.Achange(initial), target) or self.canObtain(self.Bchange(initial), target)
#    def Achange(self, string):
#        return string + 'A'
#    def Bchange(self, string):
#        return string[::-1] + 'B'
#    def test(self):
#        assert self.canObtain('A', 'BB')   == False
#        assert self.canObtain('B', 'ABBA') == True
#        assert self.canObtain('AB', 'ABB') == False
#        assert self.canObtain("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA") == True
#        return True

### Version 2

class ABBA:
    def canObtain(self, initial, target):
        dict_b2s = {True:"Possible", False:"Impossible"}
        return dict_b2s[self.canObtainRec(initial, target)]

    def canObtainRec(self, initial, target):
        def reverse(string): return string[::-1]
        def head(string): return string[0:-1]
        if len(initial) == len(target):
            return initial == target
        if target[-1] == 'A': result = self.canObtainRec(initial, head(target))
        if target[-1] == 'B': result = self.canObtainRec(initial, reverse(head(target)))
        return result

    def test(self):
        assert self.canObtain('A', 'BB')   == "Impossible"
        assert self.canObtain('B', 'ABBA') == "Possible"
        assert self.canObtain('AB', 'ABB') == "Impossible"
        assert self.canObtain("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA") == "Possible"
        return True
