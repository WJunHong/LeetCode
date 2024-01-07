class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(
            [c if c.isalnum() else "" for c in s.lower().replace(" ", "")])
        if len(s) < 2:
            return True
        else:
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
