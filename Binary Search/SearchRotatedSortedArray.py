class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if target > nums[right]:
                if nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

        return -1
