class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            volume = (right - left) * min(height[right], height[left])
            res = max(volume, res)
            if height[left] == height[right]:
                left += 1
            elif height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1

        return res

# Traverse side with smaller value to find "better" results
