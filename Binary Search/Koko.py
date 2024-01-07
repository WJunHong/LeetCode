class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        mid = 0
        while left < right:
            mid = left + (right - left) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            if total_time <= h:
                right = mid
            else:
                left = mid + 1
        return left
