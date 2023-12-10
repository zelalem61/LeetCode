class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = {}
        
        patt = list(pattern)
        si = s.split(" ")
        if len(patt) != len(si):
            return False
        for i in range(len(patt)):
            if patt[i] not in dictionary:
                if si[i] in list(dictionary.values()):
                    return False
                dictionary[patt[i]] = si[i]
            else:
                if dictionary[patt[i]] != si[i]:
                    return False
        return True