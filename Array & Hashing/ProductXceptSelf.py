class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = [0] * len(nums)
        x[0] = 1
        for i in range(1, len(x)):
            x[i] = x[i - 1] * nums[i - 1]
        rhs = 1
        for i in range(len(x) - 1, -1, -1):
            x[i] = x[i] * rhs
            rhs = rhs * nums[i]
        return x
