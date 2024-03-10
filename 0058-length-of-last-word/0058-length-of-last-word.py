class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip()
        arr = new.split(" ")
        return len(arr[-1])