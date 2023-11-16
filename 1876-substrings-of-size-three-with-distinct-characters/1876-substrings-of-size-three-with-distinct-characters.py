def good_str(s):
    stri = s.split()
    for s in stri:
        if len(s) == len(set(s)) :
            print(s)
            return True
    


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        sub_strings = []
        count = 0 
        for i in range(len(s)):
            k = s[i:i+3]
            if len(k) == 3:
                sub_strings.append(k)
                
        for sub_string in sub_strings:
            if good_str(sub_string):
                count += 1
        return count