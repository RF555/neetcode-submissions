class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        l = 0
        r = 0
        map = {}
        max_len = 1

        while r < len(s):
            if s[r] in map:
                l = map[s[r]]
                r = l + 1
                max_len = max(max_len, len(map))
                map = {}
            else:
                map[s[r]] = r
                r += 1
                max_len = max(max_len, len(map))
        return max_len
