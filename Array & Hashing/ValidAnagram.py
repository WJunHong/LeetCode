class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0] * 26
        l2 = [0] * 26
        for i in s:
            l1[ord(i) - 97] += 1
        for i in t:
            l2[ord(i) - 97] += 1
        for i in range(0, 26):
            if l1[i] != l2[i]:
                return False
        return True
