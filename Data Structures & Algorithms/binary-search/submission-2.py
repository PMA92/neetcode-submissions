class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < target:
                l += 1
            elif nums[r] > target:
                r -= 1
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l
        return -1

            