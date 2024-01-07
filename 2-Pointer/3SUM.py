class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            target = 0 - nums[i]
            if i == len(nums) - 2:
                break
            else:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == target:
                        a = [nums[i], nums[left], nums[right]]
                        a.sort()
                        if a not in res:
                            res.append(a)
                        left += 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return res

# Iterate from LHS to RHS, use curr + 2SUM
