class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        sub = [s[0]]
        best = 0
        while r < len(s):
            if s[r] not in sub:
                sub.append(s[r])
            else: 
                cut = sub.index(s[r]) + 1
                sub = sub[cut:]
                sub.append(s[r])
                l += cut        
            r += 1
            best = max(len(sub), best)
        return best