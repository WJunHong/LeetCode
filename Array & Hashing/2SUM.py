class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(zip(nums, range(0, len(nums))))
        nums.sort(key=lambda x: x[0])
        i = 0
        j = len(nums) - 1
        while True:
            if nums[i][0] + nums[j][0] == target:
                return [nums[i][1], nums[j][1]]
            elif nums[i][0] + nums[j][0] < target:
                i += 1
            else:
                j -= 1
