class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        helper_map = {}
        max_length = 0
        start = 0
        for i in range(0, len(s)):
            if s[i] not in helper_map:
                length = i - start + 1
                max_length = max(max_length, length)
            else:
                if helper_map[s[i]] >= start:
                    start = helper_map[s[i]] + 1
                else:
                    length = i - start + 1
                    max_length = max(max_length, length)
            helper_map[s[i]] = i
        return max_length
