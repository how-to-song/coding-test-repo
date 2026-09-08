class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen  = dict()
        for ch in s:
            if ch not in seen.keys():
                seen[ch] = 0
            else:
                seen[ch] += 1
        
        
        for key in seen.keys():
            if seen[key] == 0:
                for i in range(len(s)):
                    if s[i] == key: return i
        
        return -1
        
        
