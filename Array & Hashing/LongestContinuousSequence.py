class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for ele in nums:
            if ele - 1 not in nums:
                curr = 1
                y = ele + 1
                while y in nums:
                    curr += 1
                    y += 1
                best = max(best, curr)
        return best
