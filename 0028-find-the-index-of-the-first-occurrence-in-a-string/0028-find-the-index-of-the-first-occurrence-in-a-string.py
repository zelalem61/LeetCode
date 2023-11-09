class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = i
                k = 0
                
                while j < len(haystack) and k < len(needle):
                    if haystack[j] == needle[k]:
                        j += 1
                        k += 1
                    if k == len(needle):
                        return i
                    if haystack[j] != needle[k]:
                        break
                        
                    
        